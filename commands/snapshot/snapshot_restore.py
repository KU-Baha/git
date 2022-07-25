import os
import shutil
import zipfile
from pathlib import Path

from commands.snapshot.snapshot_helper import del_intermediate_dir, move_to_intermediate_dir, \
    move_back_from_intermediate_dir
from commands.utils.config import BASE_FS_PATH, SNAPSHOT_DIR_IN_INTERMEDIATE_DIR, SNAPSHOT_INTERMEDIATE_DIR


def snapshot_restore(snapshot_hash: str):
    with zipfile.ZipFile(f'{SNAPSHOT_DIR_IN_INTERMEDIATE_DIR}/{snapshot_hash}.zip', 'r') as zip_ref:
        zip_ref.extractall(BASE_FS_PATH)


def snapshot_restore_helper(*args):
    if len(args) != 1:
        print("Command 'snapshot create' take one argument! - 'snapshot' argument!")
        return False

    snapshot_hash = args[0]

    if Path(SNAPSHOT_INTERMEDIATE_DIR).is_dir():
        del_intermediate_dir()

    move_to_intermediate_dir()

    snapshot_restore(snapshot_hash)

    move_back_from_intermediate_dir()
    del_intermediate_dir()

    print('Snapshot success restore!')

    return True
