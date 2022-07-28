import os
import shutil

from commands.add_file import add_file
from commands.del_file import del_file
from commands.restore import restore
from commands.utils.config import SNAPSHOT_DIR_PATH, INTERMEDIATE_DIR, INTERMEDIATE_DATABASE, INTERMEDIATE_OBJECTS
from commands.utils.database_helper import database_list, delete_from_database, get_data_by_key, hash_file, \
    add_to_database
from commands.utils.fs_helper import check_file, del_intermediate_dir


def commit_helper(*args) -> None:
    if len(args) != 3:
        print("Command 'commit' takes 3 arguments - snapshot, file_path, file_in_snapshot")
        return

    snapshot, file_path, file_in_snapshot = args

    snapshot_path = f'{SNAPSHOT_DIR_PATH}/{snapshot}.zip'

    if not check_file(snapshot_path):
        print("Snapshot not found!")
        return

    if not check_file(file_path):
        print("File not found!")
        return

    restore(snapshot_path, INTERMEDIATE_DIR)

    database = database_list(INTERMEDIATE_DATABASE)

    data = delete_from_database(file_in_snapshot, database, INTERMEDIATE_DATABASE)

    if not data:
        print("File not found in snapshot!")
        return

    d_file_hash, d_file_path = data

    if not get_data_by_key(d_file_hash, database):
        file_path_in_fs = os.path.join(INTERMEDIATE_OBJECTS, d_file_hash)

        if check_file(file_path_in_fs):
            del_file(file_path_in_fs)

    file_hash = hash_file(file_path)

    if not add_to_database(file_hash, file_in_snapshot, database, INTERMEDIATE_DATABASE):
        print("File already exists in database!")
        return

    add_file(file_path, file_hash, INTERMEDIATE_OBJECTS)

    shutil.make_archive(f"{SNAPSHOT_DIR_PATH}/{snapshot}", "zip", INTERMEDIATE_DIR)

    del_intermediate_dir()

    print("Success commited!")