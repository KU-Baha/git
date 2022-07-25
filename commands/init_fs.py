import sys
from pathlib import Path
import os

from commands.utils.config import *
from commands.utils.hook_helper import create_hook_structure


def init_fs(called_path: str) -> None:
    fs_path = os.path.join(called_path, FS_OBJECTS)
    db_path = os.path.join(called_path, DATABASE_PATH)
    list_path = os.path.join(called_path, LIST_FILE_PATH)
    log_file = os.path.join(called_path, SNAPSHOTS_DB_PATH)
    snapshot_path = os.path.join(called_path, SNAPSHOT_DIR_PATH)

    os.makedirs(fs_path, exist_ok=True)
    os.makedirs(snapshot_path, exist_ok=True)

    Path(list_path).touch(exist_ok=True)
    Path(log_file).touch(exist_ok=True)
    Path(db_path).touch(exist_ok=True)

    print("FS success initialized!")


def init_fs_helper(*args) -> bool:
    if len(args) != 0:
        print("Command 'init' doesn't take any arguments!")
        return False

    called_path = os.getcwd()
    init_path = os.path.join(called_path, BASE_FS_PATH)

    if Path(init_path).is_dir():
        print("FS already initialized!")
        return False

    init_fs(called_path)
    create_hook_structure()

    return True


if __name__ == '__main__':
    _, *args = sys.argv
    init_fs_helper(*args)
