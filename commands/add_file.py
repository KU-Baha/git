import sys
from pathlib import Path
import os
import shutil

from utils.config import *
from utils.database_helper import hash_file, add_to_database, database_list
from utils.fs_helper import check_file


def add_file(file_from: str, file_hash: str):
    file_to = os.path.join(FS_OBJECTS, file_hash)

    shutil.copyfile(file_from, file_to)


def add_file_helper(*args) -> bool:
    if len(args) == 0 or len(args) > 2:
        print("Command 'add' take 1 or 2 argument - file path, new file path!")
        return False

    called_path = os.getcwd()
    file_path = args[0]

    if not check_file(file_path):
        print("File not found!")
        return False

    database = database_list()

    # Check in database before adding to FS

    new_file_path = os.path.join(called_path, file_path).lstrip('/')
    file_name = Path(new_file_path).name
    file_hash = hash_file(file_path)

    if len(args) == 2:
        new_file_path = args[1].lstrip('/')

        if new_file_path[-1] == '/':
            new_file_path = new_file_path + file_name

    if not add_to_database(file_hash, new_file_path, database):
        # Run deleting file in objects
        print("File already exists in database!")
        return False

    print('Success added to database!')

    file_path = os.path.join(called_path, file_path)

    add_file(file_path, file_hash)
    print('Success added to FS!')

    return True


if __name__ == '__main__':
    _, *args = sys.argv
    add_file_helper(*args)
