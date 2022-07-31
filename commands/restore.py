import zipfile
import shutil
from pathlib import Path

from commands.utils.config import BASE_FS_PATH, BASE_FS_COPY


def restore(backup_path: str, extract_dir):
    with zipfile.ZipFile(backup_path) as my_zip:
        my_zip.extractall(extract_dir)


def restore_helper(*args) -> None:
    if len(args) != 1:
        print("Command 'backup' take 1 argument - backup_path!")
        return

    backup_path = args[0]

    if not zipfile.is_zipfile(backup_path):
        print("File not found!")
        return

    shutil.copytree(BASE_FS_PATH, BASE_FS_COPY, dirs_exist_ok=True)

    shutil.rmtree(BASE_FS_PATH, ignore_errors=True)

    restore(backup_path, BASE_FS_PATH)

    if not Path(BASE_FS_PATH).is_dir():
        print("Error with restore!")
        shutil.copytree(BASE_FS_COPY, BASE_FS_PATH, dirs_exist_ok=True)

    shutil.rmtree(BASE_FS_COPY, ignore_errors=True)

    # create_hook_structure()
