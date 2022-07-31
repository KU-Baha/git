import shutil
from pathlib import Path

from commands.utils.config import SNAPSHOT_DIR_PATH, INTERMEDIATE_DIR, INTERMEDIATE_OBJECTS, CHECKOUT_DIRS, \
    DATABASE_NAME
from commands.utils.database_helper import database_list, get_data_by_key
from commands.utils.fs_helper import check_file, get_file_in_snapshot, del_intermediate_dir


def checkout_helper(*args) -> None:
    if len(args) != 2:
        print("Command 'checkout' takes 2 arguments - snapshot, file_path")
        return

    snapshot, file_path = args

    snapshot_path = f'{SNAPSHOT_DIR_PATH}/{snapshot}.zip'

    if not check_file(snapshot_path):
        print("Snapshot not found!")
        return

    get_file_in_snapshot(snapshot_path, DATABASE_NAME)

    database = database_list(f"{INTERMEDIATE_DIR}/{DATABASE_NAME}")

    data = get_data_by_key(file_path, database)

    if not data:
        print("File not found in snapshot!")
        del_intermediate_dir()
        return

    file_hash = data.get('file_hash')

    get_file_in_snapshot(snapshot_path, f'objects/{file_hash}')

    directories = '/'.join(file_path.split('/')[:-1])

    Path(f"{CHECKOUT_DIRS}/{directories}").mkdir(parents=True, exist_ok=True)
    shutil.move(f"{INTERMEDIATE_OBJECTS}/{file_hash}", f"{CHECKOUT_DIRS}/{file_path}")

    del_intermediate_dir()
