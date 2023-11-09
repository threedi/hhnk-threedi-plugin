import numpy as np
from hhnk_threedi_tools.variables.definitions import proposed_value_col
from PyQt5.QtCore import QAbstractTableModel, QSortFilterProxyModel, Qt, QVariant
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QLabel, QLineEdit, QTableView, QVBoxLayout, QWidget


class pandasModel(QAbstractTableModel):
    """
    Model to display dataframe as a table to the user.
    """

    def __init__(
        self,
        data,
        old_col_idx,
        new_col_idx,
        id_col,
        delete_rows_ids,
        add_rows_ids,
        new_col_editable,
        rows_selectable,
    ):
        super(pandasModel, self).__init__()
        self.sortRole = Qt.UserRole + 1
        self._data = data
        self.old_col_idx = old_col_idx
        self.new_col_idx = new_col_idx
        self.id_col_ind = self._data.columns.get_loc(id_col)
        self.delete_rows_ids = delete_rows_ids
        self.add_rows_ids = add_rows_ids
        self.new_col_editable = new_col_editable
        self.rows_selectable = rows_selectable
        self.num_rows, self.num_cols = self._data.shape
        self.red = QColor().fromRgb(231, 76, 60, 255)
        self.green = QColor().fromRgb(46, 204, 113, 255)

    def rowCount(self, parent=None):
        return self.num_rows

    def columnCount(self, parent=None):
        return self.num_cols

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == self.sortRole:
                """
                Sorting by default assumes all data is a string, which leads to unexpected results when
                sorting integers or floats. We make sure data is correctly interpreted here.
                """
                try:
                    value = float(self._data.iloc[index.row(), index.column()])
                except:
                    try:
                        value = int(self._data.iloc[index.row(), index.column()])
                    except:
                        value = self._data.iloc[index.row(), index.column()]
                return value
            if self.rows_selectable:
                """
                If rows are selectable, the first column consists if checkboxes. We have to check the bool value
                in the model and return the corresponding Checkstate to display.
                """
                if index.column() == 0:
                    if role == Qt.CheckStateRole:
                        value = self._data.iloc[index.row(), index.column()]
                        return Qt.Checked if value else Qt.Unchecked
            if role in (Qt.DisplayRole, Qt.EditRole):
                return QVariant(str(self._data.iloc[index.row(), index.column()]))
            if self.old_col_idx is not None:
                """Old value cells are coloured red"""
                if (
                    role == Qt.BackgroundRole
                    and index.column() == self.old_col_idx
                    and self._data.iloc[index.row(), self.id_col_ind] not in self.delete_rows_ids
                ):
                    return self.red
            if self.new_col_idx is not None:
                """New value cells are coloured green"""
                if (
                    role == Qt.BackgroundRole
                    and index.column() == self.new_col_idx
                    and self._data.iloc[index.row(), self.id_col_ind] not in self.delete_rows_ids
                ):
                    return self.green
            if self.delete_rows_ids is not None:
                """Rows to be deleted are coloured red"""
                if role == Qt.BackgroundRole and self._data.iloc[index.row(), self.id_col_ind] in self.delete_rows_ids:
                    return self.red
            if self.add_rows_ids is not None:
                """Rows to be added are coloured green"""
                if role == Qt.BackgroundRole and self._data.iloc[index.row(), self.id_col_ind] in self.add_rows_ids:
                    return self.green
        return QVariant()

    def headerData(self, col, orientation, role):
        """Add column names to the model"""
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None

    def setData(self, index, value, role=Qt.EditRole):
        """mod
        If data is edited, this function is called to handle setting it to the display model depending on the
        specified role
        """

        def convert_to_type(type_val, val):
            """type_val is the column type, val is the value the user supplied. We try to convert
            the val to the column value. If that is not possible, we set the cell to 'Invalid'"""
            try:
                if type_val in (float, np.float64, np.int32):
                    return float(val)
                if type_val in (int, np.int64, np.int32):
                    return int(val)
                else:
                    return val
            except:
                return "Invalid"

        if not index.isValid():
            return False
        if role not in (Qt.EditRole, Qt.CheckStateRole):
            return False
        row = index.row()
        if row < 0 or row >= self._data.shape[0]:
            return False
        column = index.column()
        if column < 0 or column >= self._data.shape[1]:
            return False
        if role == Qt.CheckStateRole:
            """If the cell contains a checkbox, we have set the new data as a bool to the model"""
            self._data.iloc[index.row(), index.column()] = bool(value)
            self.dataChanged.emit(index, index)
            return True
        if role == Qt.EditRole:
            """If the cell is editable, we receive the new data as a string, then try to convert it to the type
            of the column"""
            self._data.iloc[row, column] = convert_to_type(type(self._data.iloc[row, column]), value)
            self.dataChanged.emit(index, index)
            return True
        return False

    def flags(self, index):
        flags = Qt.ItemIsEnabled
        if self.rows_selectable:
            """If rows are selectable, the first row is used to select rows and contains checkboxes"""
            if index.column() == 0:
                if (
                    (
                        self.delete_rows_ids is not None
                        and self._data.iloc[index.row(), self.id_col_ind] in self.delete_rows_ids
                    )
                    or (
                        self.add_rows_ids is not None
                        and self._data.iloc[index.row(), self.id_col_ind] in self.add_rows_ids
                    )
                    or self.new_col_editable
                ):
                    flags |= Qt.ItemIsUserCheckable
        if (
            index.column() == self.new_col_idx
            and self.new_col_editable
            and (not self.add_rows_ids or self._data.iloc[index.row(), self.id_col_ind] in self.add_rows_ids)
        ):
            """If cells are in the column containing new values and that column is editable, make te cell
            editable if we are not adding rows. If we are adding rows, we first make sure the id is in the rows
            we are going to add."""
            flags |= Qt.ItemIsEditable
        return flags


class modelChangesPreview(QWidget):
    """
    Class that allows users to preview and edit (either change values or choose which changes not to make)
    the proposed changes to the model database

    modelChangesPreview(
        window_title    str
        description     str
        df              pandas dataframe or geopandas geodataframe - (dataframe containing proposed changes as table),
        id_col          str - name of identifying column in df,
        old_col         str - name of column containing values we will replace -> None,
        new_col         str - name of column containing values replacing the old values -> None,
        delete_rows_ids list - ids (in id_col) marked for deletion -> [],
        add_rows_ids    list - ids (in id_col) corresponding to rows marked for adding -> [],
        new_col_editable bool - whether or not column containing new values is editable -> False
        rows_selectable bool - whether or not a user can exclude rows -> False
        searchable      bool - whether or not a searchbar is added that allows users to search the id_col
    )
    """

    def __init__(
        self,
        window_title,
        description,
        df,
        id_col,
        old_col=None,
        new_col=None,
        delete_rows_ids=[],
        add_rows_ids=[],
        new_col_editable=False,
        rows_selectable=False,
        searchable=False,
    ):
        super(modelChangesPreview, self).__init__()
        self.setWindowTitle(window_title)
        description_label = QLabel(description)
        self.df = df
        self.id_col = id_col
        self.id_col_idx = self.df.columns.get_loc(id_col)
        if old_col is not None:
            self.old_col_idx = self.df.columns.get_loc(old_col)
        else:
            self.old_col_idx = None
        if new_col is not None:
            self.new_col_idx = self.df.columns.get_loc(new_col)
        else:
            self.new_col_idx = None
        self.delete_rows_ids = delete_rows_ids
        self.add_rows_ids = add_rows_ids
        self.new_col_editable = new_col_editable
        self.rows_selectable = rows_selectable
        self.searchable = searchable
        if new_col_editable:
            """If the new column is editable, we make a copy of the current dataframe
            so we can compare the proposed changes to the manual changes the user made
            for logging purposes"""
            self.df_before = self.df.copy()
        if self.rows_selectable:
            """If rows are selectable, we add a row of checkboxes at the start of the
            dataframe and set their state based on whether an id is in the list of ids we are
            either adding or deleting"""
            self.df.insert(0, "select", True)
            if self.add_rows_ids:
                self.df["select"] = self.df[id_col].isin(self.add_rows_ids)
            if self.delete_rows_ids:
                self.df["select"] = self.df[id_col].isin(self.delete_rows_ids)
            if self.new_col_editable or self.new_col_idx is not None:
                self.old_col_idx += 1
                self.new_col_idx += 1
            self.id_col_idx += 1
        # Df in which we collect manual changes made by the user and proposed values
        self.manual_changes_df = None
        # List of ids a user has excluded from either being added or deleted
        self.protected_ids_list = []
        self.keep_rows_df = None
        layout = QVBoxLayout()
        if self.searchable:
            """Adds a search bar to widget which allows a user to search the id_col"""
            self.search_bar_label = QLabel(f"Search {id_col}")
            self.search_bar = QLineEdit("")
        # Adds the dataframe model to the widget
        self.view = QTableView()
        model = pandasModel(
            self.df,
            old_col_idx=self.old_col_idx,
            new_col_idx=self.new_col_idx,
            id_col=self.id_col,
            delete_rows_ids=delete_rows_ids,
            add_rows_ids=add_rows_ids,
            new_col_editable=new_col_editable,
            rows_selectable=rows_selectable,
        )
        # Allows sorting by clicking on a column header
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setDynamicSortFilter(False)
        self.proxy_model.setSourceModel(model)
        self.proxy_model.setSortRole(model.sortRole)
        # Sets column to be searched by the search bar
        self.proxy_model.setFilterKeyColumn(self.df.columns.get_loc(self.id_col))
        self.view.setModel(self.proxy_model)
        self.view.setSortingEnabled(True)
        self.view.sortByColumn(self.id_col_idx, Qt.AscendingOrder)
        layout.addWidget(description_label)
        if self.searchable:
            """Implements the actual searching functionality"""
            self.search_bar.textChanged.connect(lambda: self.proxy_model.setFilterRegExp(f"{self.search_bar.text()}"))
            layout.addWidget(self.search_bar_label)
            layout.addWidget(self.search_bar)
        layout.addWidget(self.view)
        self.setLayout(layout)

    def return_changed_value_rows(self):
        """
        Returns information about manually changed fields and the automatically generated values
        as well as the rows that were excluded from updating
        """
        if self.rows_selectable or self.new_col_editable:
            protected_ids = self.df[~self.df["select"]].iloc[:, self.id_col_idx].tolist()
            self.protected_ids_list = protected_ids

        if self.new_col_editable:
            new_val_col = self.df.columns[self.new_col_idx]
            combine = self.df
            combine[proposed_value_col] = self.df_before[new_val_col]
            changed_rows = combine[combine[new_val_col] != combine[proposed_value_col]]
            changed_rows = changed_rows[~changed_rows[self.id_col].isin(self.protected_ids_list)]
            self.manual_changes_df = changed_rows
