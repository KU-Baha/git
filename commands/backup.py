import shutil
from commands.utils.config import BASE_FS_PATH
import time


def backup(path_to: str):
    shutil.make_archive(f'{path_to}/zeon_git_backup_{time.time()}', 'zip', BASE_FS_PATH)


def backup_helper(*args):
    if len(args) != 1:
        print("Command 'backup' take 1 argument - patht_to!")
        return False

    path_to = args[0]

    backup(path_to)
