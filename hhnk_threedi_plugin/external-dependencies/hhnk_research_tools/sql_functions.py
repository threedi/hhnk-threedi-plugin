import sqlite3
import pandas as pd
import geopandas as gpd
import os
from hhnk_research_tools.variables import MOD_SPATIALITE_PATH, DEF_SRC_CRS
from hhnk_research_tools.dataframe_functions import df_convert_to_gdf

# TODO was: create_update_case_statement
def sql_create_update_case_statement(
    df,
    layer,
    df_id_col,
    db_id_col,
    new_val_col,
    excluded_ids=[],
    old_val_col=None,
    old_col_name=None,
    show_prev=False,
    show_proposed=False,
) -> str:
    """
    Creates an sql statement with the following structure:
    UPDATE (table_name)
    SET (database_column_to_change) = CASE (database_id_col)
    WHEN (id) THEN (new value associated with id) OPTIONAL -- ['Previous' or 'Proposed'] previous or proposed value

    Initialization:

    """
    if show_proposed and show_prev:
        raise Exception(
            "sql_create_update_case_statement: "
            "Only one of show_prev and show_proposed can be True"
        )
    try:
        query = None
        if not show_prev and not show_proposed:
            vals_list = [
                (idx, val)
                for idx, val in zip(df[df_id_col], df[new_val_col])
                if idx not in excluded_ids
            ]
            statement_list = [
                f"WHEN {idx} THEN {val if not val is None else 'null'}"
                for idx, val in vals_list
            ]
        else:
            comment = "Previous:" if show_prev else "Proposed"
            vals_list = [
                (old_val, new_val, cur_id)
                for old_val, new_val, cur_id in zip(
                    df[old_val_col], df[new_val_col], df[df_id_col]
                )
                if cur_id not in excluded_ids
            ]
            statement_list = [
                f"WHEN {cur_id} THEN {new_val if not new_val is None else 'null'} -- {comment} {old_val}"
                for old_val, new_val, cur_id in vals_list
            ]
        if statement_list:
            statement_string = "\n".join(statement_list)
            query = f"""
            UPDATE {layer}
            SET {old_col_name if old_col_name is not None else old_val_col} = CASE {db_id_col}
            {statement_string}
            ELSE {old_val_col}
            END
            """
        return query
    except Exception as e:
        raise e from None


# TODO was: construct_select_query
def sql_construct_select_query(table, columns=None) -> str:
    """
    This functions constructs sql queries that select either all
    or specified columns from a table.

    Columns has to be a list. If a list item is a tuple, it will be interpreted as:
    (column, alias). In other cases, we assume the item to be a valid column name.
    """
    base_query = "SELECT {columns} \nFROM {table}"
    try:
        if columns is not None:
            selection_lst = []
            if type(columns) == dict:
                for key, value in columns.items():
                    if value is not None:
                        selection_lst.append(f"{key} AS {value}")
                    else:
                        selection_lst.append(key)
            elif type(columns) == list:
                selection_lst = columns
            query = base_query.format(columns=",\n".join(selection_lst), table=table)
        else:
            query = base_query.format(columns="*", table=table)
        return query
    except Exception as e:
        raise e from None


def create_sqlite_connection(database_path):
    """Create connection to database. On windows with conda envs this requires the mod_spatialaite extension
    to be installed explicitly. The location of this extension is stored in
    hhnk_research_tools.variables.MOD_SPATIALITE_PATH (C:\ProgramData\Anaconda3\mod_spatialite-5.0.1-win-amd64)
    and can be downloaded from http://www.gaia-gis.it/gaia-sins/windows-bin-amd64/"""
    try:
        conn = sqlite3.connect(database_path)
        conn.enable_load_extension(True)
        conn.execute("SELECT load_extension('mod_spatialite')")
        return conn
    except sqlite3.OperationalError as e:
        if e.args[0] == "The specified module could not be found.\r\n":
            if os.path.exists(MOD_SPATIALITE_PATH):
                os.environ["PATH"] = MOD_SPATIALITE_PATH + ";" + os.environ["PATH"]

                conn = sqlite3.connect(database_path)
                conn.enable_load_extension(True)
                conn.execute("SELECT load_extension('mod_spatialite')")
                return conn
            else:
                print(
                    """Download mod_spatialite extension from http://www.gaia-gis.it/gaia-sins/windows-bin-amd64/ 
                and place into anaconda installation C:\ProgramData\Anaconda3\mod_spatialite-5.0.1-win-amd64."""
                )
                raise e from None

    except Exception as e:
        raise e from None


# TODO was: table_exists
def sql_table_exists(database_path, table_name):
    """
    Checks if a table name exists in the specified database
    """
    try:
        query = f"""PRAGMA table_info({table_name})"""
        df = execute_sql_selection(query=query, database_path=database_path)
        return not df.empty
    except Exception as e:
        raise e from None


def execute_sql_selection(
    query, conn=None, database_path=None, **kwargs
) -> pd.DataFrame:
    """
    Execute sql query. Creates own connection if database path is given.
    Returns pandas dataframe
    """
    kill_connection = conn is None
    try:
        if database_path is None and conn is None:
            raise Exception("No connection or database path provided")
        if database_path is not None:
            conn = create_sqlite_connection(database_path=database_path)
        db = pd.read_sql(query, conn, **kwargs)
        return db
    except Exception as e:
        raise e from None
    finally:
        if kill_connection and conn is not None:
            conn.close()


def execute_sql_changes(query, database=None, conn=None):
    """
    Takes a query that changes the database and tries
    to execute it. On success, changes are committed.
    On a failure, rolls back to the state before
    the query was executed that caused the error

    The explicit begin and commit statements are necessary
    to make sure we can roll back the transaction
    """
    conn_given = True
    try:
        if not conn:
            conn_given = False
            conn = create_sqlite_connection(database)
        try:
            conn.executescript(f"BEGIN; {query}; COMMIT")
        except Exception as e:
            conn.rollback()
            raise e from None
    except Exception as e:
        raise e from None
    finally:
        if not conn_given and conn:
            conn.close()


# TODO was: get_creation_statement_from_table
def _sql_get_creation_statement_from_table(src_table_name, dst_table_name, cursor):
    """ "Replace the original table name with the new name to make the creation statement"""
    try:
        creation_sql = f"""
                    SELECT sql
                    FROM sqlite_master
                    WHERE type = 'table'
                    AND name = '{src_table_name}'
                    """

        create_statement = cursor.execute(creation_sql).fetchone()[0]
        to_list = create_statement.split()
        all_but_name = [
            item if index != 2 else f'"{dst_table_name}"'
            for index, item in enumerate(to_list)
        ]
        creation_statement = " ".join(all_but_name)
        return creation_statement
    except Exception as e:
        raise e from None


# TODO was: replace_or_add_table
def sqlite_replace_or_add_table(
    db, dst_table_name, src_table_name, select_statement=None
):
    """
    This functions maintains the backup tables.
    Tables are created if they do not exist yet.
    After that, rows are replaced if their id is already
    in the backup, otherwise they are just inserted.

    columns HAS to be a list of tuples containing the name
    of the column and it's type
    """
    try:
        query_list = []
        conn = create_sqlite_connection(database_path=db)
        curr = conn.cursor()
        # Check if table exists
        exists = curr.execute(
            f"SELECT count() from sqlite_master "
            f"WHERE type='table' and name='{dst_table_name}'"
        ).fetchone()[0]
        if exists == 0:
            # Get the original creation statement from the table we are backing up if the new table doesn't exist
            if select_statement is None:
                select_statement = f"SELECT * from {src_table_name}"
            creation_statement = _sql_get_creation_statement_from_table(
                src_table_name=src_table_name,
                dst_table_name=dst_table_name,
                cursor=curr,
            )
            query_list.append(creation_statement)
            # Create the statement that copies the columns specified in select statement or copies the entire table
            copy_statement = f"INSERT INTO {dst_table_name} {select_statement}"
            query_list.append(copy_statement)
            query = ";\n".join(query_list)
        else:
            # If the backup table exists, we replace any rows that are changed since last backup
            query = f"REPLACE INTO {dst_table_name} " f"SELECT * from {src_table_name}"
        execute_sql_changes(query=query, conn=conn)
    except Exception as e:
        raise e from None
    finally:
        if conn:
            conn.close()


# TODO was: get_table_as_df
def sqlite_table_to_df(database_path, table_name, columns=None) -> pd.DataFrame:
    conn = None
    try:
        conn = create_sqlite_connection(database_path=database_path)
        query = sql_construct_select_query(table_name, columns)
        df = execute_sql_selection(query=query, conn=conn)
        return df
    except Exception as e:
        raise e from None
    finally:
        if conn:
            conn.close()


# TODO was: gdf_from_sql
def sqlite_table_to_gdf(
    query, id_col, to_gdf=True, conn=None, database_path=None
) -> gpd.GeoDataFrame:
    """
    Returns DataFrame or GeoDataFrame from database query.

        sqlite_table_to_gdf(
                query (string)
                id_col (identifying column)
                to_gdf -> True (if False, DataFrame is returned)
                conn -> None (sqlite3 connection object)
                database_path -> None (path to database)

                Supply either conn or database path.
                )
    """
    if (conn is None and database_path is None) or (
        conn is not None and database_path is not None
    ):
        raise Exception("Provide exactly one of conn or database_path")
    try:
        kill_conn = conn is None
        if conn is None:
            conn = create_sqlite_connection(database_path=database_path)
        df = execute_sql_selection(query=query, conn=conn)
        if to_gdf:
            df = df_convert_to_gdf(df=df, src_crs=DEF_SRC_CRS)
        df.set_index(id_col, drop=False, inplace=True)
        return df
    except Exception as e:
        raise e from None
    finally:
        if kill_conn and conn is not None:
            conn.close()
