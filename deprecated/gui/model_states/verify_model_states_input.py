from ..path_verification_functions import (
    is_valid_model_path,
    is_valid_geodatabase_path,
    is_valid_results_folder,
)
from ...error_messages.input_error_messages import (
    invalid_model_path,
    no_bank_levels_calculated,
    no_manholes_backup,
    invalid_datachecker_path,
    invalid_threedi_result,
    from_and_to_states_same,
)

# hhnk-research-tools
import hhnk_research_tools as hrt

# hhnk-threedi-tests
from hhnk_threedi_tools.variables.model_state import (
    hydraulic_test_state,
    one_d_two_d_state,
    one_d_two_d_keep,
    one_d_two_d_from_calc,
)
from hhnk_threedi_tools.variables.backups_table_names import (
    MANHOLES_TABLE,
    BANK_LVLS_LAST_CALC,
)


def verify_input(
    model_path,
    from_state,
    to_state,
    one_d_two_d_from=None,
    threedi_result_folder=None,
    datachecker_path=None,
):
    """
    Checks whether all fields are correctly filled out

    verify_input(model_path, from_state, to_state, one_d_two_d_from -> None,
                threedi_result_folder -> None, datachecker_path -> None)

    return values: valid_input (bool), error_message (empty string if no error, else message to display)
    """
    if not is_valid_model_path(model_path):
        return False, invalid_model_path.format(model_path)
    if to_state == from_state:
        return False, from_and_to_states_same
    else:
        if to_state == hydraulic_test_state:
            return True, ""
        elif to_state == one_d_two_d_state:
            if one_d_two_d_from == one_d_two_d_keep:
                if not hrt.sql_table_exists(model_path, BANK_LVLS_LAST_CALC):
                    return False, no_bank_levels_calculated
                # if not hrt.sql_table_exists(model_path, MANHOLES_TABLE):
                #     return False, no_manholes_backup
            elif one_d_two_d_from == one_d_two_d_from_calc:
                if not is_valid_geodatabase_path(datachecker_path):
                    return False, invalid_datachecker_path.format(datachecker_path)
                if not is_valid_results_folder(threedi_result_folder):
                    return False, invalid_threedi_result.format(threedi_result_folder)
    return True, ""
