import sys
from pathlib import Path
import os
import shutil

from commands.utils.config import FS_OBJECTS
from commands.utils.database_helper import hash_file, add_to_database, database_list
from commands.utils.fs_helper import check_file, check_inited
from commands.list_files import list_file_helper


def add_file(file_from: str, file_hash: str):
    file_to = os.path.join(FS_OBJECTS, file_hash)

    shutil.copyfile(file_from, file_to)


def add_file_helper(*args) -> bool:
    if len(args) == 0 or len(args) > 2:
        print("Command 'add' take 1 or 2 argument - file path, new file path!")
        return False

    if not check_inited():
        print('FS not initiazlized!')
        return False

    called_path = os.getcwd()
    file_path = args[0]

    if not check_file(file_path):
        print("File not found!")
        return False

    database = database_list()

    file_name = Path(file_path).name
    file_hash = hash_file(file_path)
    new_file_path = file_name

    if len(args) == 2:
        file_to = args[1]

        new_file_path = file_to.lstrip('/')

        if not new_file_path:
            new_file_path = '/'

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

    list_file_helper()
    return True


if __name__ == '__main__':
    _, *args = sys.argv
    add_file_helper(*args)
