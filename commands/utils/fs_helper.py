import os
import shutil
import zipfile
from pathlib import Path

from commands.utils.config import BASE_FS_PATH, INTERMEDIATE_DIR


def get_file_in_snapshot(snapshot_path, file_path):
    with zipfile.ZipFile(snapshot_path, 'r') as zip_ref:
        zip_ref.extract(file_path, INTERMEDIATE_DIR)


# def add_file_to_snapshot(snapshot_path, file_from, file_to):
#     with zipfile.ZipFile(snapshot_path, 'a') as zip_ref:
#         zip_ref.write(file_from, file_to)


def del_intermediate_dir():
    shutil.rmtree(INTERMEDIATE_DIR, ignore_errors=True)


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


def check_inited():
    if not Path(BASE_FS_PATH).is_dir():
        return False

    return True
