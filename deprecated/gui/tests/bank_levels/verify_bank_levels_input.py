from ....gui.path_verification_functions import (
    is_valid_model_path,
)
from ....error_messages.input_error_messages import (
    invalid_model_path,
)


def verify_input(model_path):
    """
    Checks whether all provided input is valid

    verify_input(model_path, datachecker_path, output_path, revision_selected (name of folder))

    return values: valid_input (bool), error_message (empty string if no error)
    """
    if not is_valid_model_path(model_path):
        return False, invalid_model_path.format(model_path)
    return True, ""
