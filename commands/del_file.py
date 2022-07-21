import os
import sys

from commands.list_files import list_file_helper
from commands.utils.database_helper import *
from commands.utils.fs_helper import check_inited


def del_file(file_path: str) -> None:
    os.remove(file_path)


def del_file_helper(*args) -> bool:

    if len(args) != 1:
        print("Command 'del' take 1 argument - file path!")
        return False

    if not check_inited():
        print('FS not initiazlized!')
        return False

    file_path = args[0]

    database = database_list()

    if not check_in_database(file_path, database):
        print('File not found in database!')
        return False

    d_file_hash, d_file_path = delete_from_database(file_path, database)

    if not get_data_by_key(d_file_hash, database):
        file_path_in_fs = os.path.join(FS_OBJECTS, d_file_hash)
        del_file(file_path_in_fs)

    list_file_helper()

    print('Success deleted!')

    return True


if __name__ == '__main__':
    _, *args = sys.argv
    del_file_helper(*args)
