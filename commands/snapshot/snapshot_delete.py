import os

from commands.snapshot.snapshot_db import snapshot_delete_from_db, snapshot_get_database, snapshot_check_in_db
from commands.utils.config import SNAPSHOT_DIR_PATH
from commands.utils.fs_helper import check_file


def snapshot_delete(snapshot_path: str):
    os.remove(snapshot_path)


def snapshot_delete_helper(*args):
    if len(args) != 1:
        print("Command 'snapshot delete' takes 1 argument - snapshot")
        return

    snapshot = args[0]
    database = snapshot_get_database()

    if not snapshot_check_in_db(snapshot, database):
        print("Snapshot not found in database!")
        return

    snapshot_path = f"{SNAPSHOT_DIR_PATH}/{snapshot}.zip"

    if not check_file(snapshot_path):
        print("Snapshot not found!")
        return

    snapshot_delete(snapshot_path)
    snapshot_delete_from_db(snapshot, database)
    print("Snapshot success deleted!")
