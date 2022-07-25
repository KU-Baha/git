import os
import shutil

from pathlib import Path

from commands.utils.config import *


def move_to_intermediate_dir():
    os.mkdir(SNAPSHOT_INTERMEDIATE_DIR)
    shutil.move(SNAPSHOT_DIR_PATH, SNAPSHOT_INTERMEDIATE_DIR)
    shutil.move(SNAPSHOTS_DB_PATH, SNAPSHOT_INTERMEDIATE_DIR)


def move_back_from_intermediate_dir():
    shutil.move(SNAPSHOT_DIR_IN_INTERMEDIATE_DIR, BASE_FS_PATH)
    shutil.move(SNAPSHOT_DB_IN_INTERMEDIATE_DIR, BASE_FS_PATH)


def del_intermediate_dir():
    if not Path(SNAPSHOT_INTERMEDIATE_DIR).is_dir():
        return

    shutil.rmtree(SNAPSHOT_INTERMEDIATE_DIR)
