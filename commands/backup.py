import os

from commands.utils.config import DATABASE_PATH, FS_OBJECTS, LIST_FILE_PATH
from zipfile import ZipFile
import time

from commands.utils.fs_helper import check_inited


def backup(path_to: str):
    with ZipFile(f'{path_to}/zeon_git_backup_{time.time()}.zip', 'w') as my_zip:
        my_zip.write(DATABASE_PATH)
        my_zip.write(LIST_FILE_PATH)

        paths = os.listdir(FS_OBJECTS)

        for path in paths:
            my_zip.write(f'{FS_OBJECTS}/{path}')


def backup_helper(*args):
    if len(args) != 1:
        print("Command 'backup' take 1 argument - patht_to!")
        return False

    if not check_inited():
        print('FS not initialized!')
        return False

    path_to = args[0]

    backup(path_to)
