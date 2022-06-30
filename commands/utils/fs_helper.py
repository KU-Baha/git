import os
from pathlib import Path


def check_file(file_path: str) -> bool:
    """
    :param file_path:
    :return: if file found return True else return False
    """

    if Path(file_path).is_absolute():
        if Path(file_path).is_file():
            return True

        return False

    file = os.path.join(os.getcwd(), file_path)

    if Path(file).is_file():
        return True

    return False
