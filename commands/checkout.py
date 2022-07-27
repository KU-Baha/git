import shutil
import zipfile
from pathlib import Path

from commands.utils.config import SNAPSHOT_DIR_PATH, INTERMEDIATE_DIR, INTERMEDIATE_OBJECTS, CHECKOUT_DIRS
from commands.utils.database_helper import database_list, get_data_by_key
from commands.utils.fs_helper import check_file


def checkout_get_in_database(snapshot_path, file_path):
    with zipfile.ZipFile(snapshot_path, 'r') as zip_ref:
        zip_ref.extract(file_path, INTERMEDIATE_DIR)


def checkout_del_dir():
    shutil.rmtree(INTERMEDIATE_DIR, ignore_errors=True)


def checkout_helper(*args) -> None:
    if len(args) != 2:
        print("Command 'checkout' takes 2 arguments - snapshot, file_path")
        return

    snapshot_hash, file_path = args

    snapshot_path = f'{SNAPSHOT_DIR_PATH}/{snapshot_hash}.zip'

    if not check_file(snapshot_path):
        print("Snapshot not found!")
        return

    checkout_get_in_database(snapshot_path, 'index')

    database = database_list(f"{INTERMEDIATE_DIR}/index")

    data = get_data_by_key(file_path, database)

    if not data:
        print("File not found!")
        checkout_del_dir()
        return

    file_hash = data.get('file_hash')

    checkout_get_in_database(snapshot_path, f'objects/{file_hash}')

    directories = '/'.join(file_path.split('/')[:-1])

    Path(f"{CHECKOUT_DIRS}/{directories}").mkdir(parents=True, exist_ok=True)
    shutil.move(f"{INTERMEDIATE_OBJECTS}/{file_hash}", f"{CHECKOUT_DIRS}/{file_path}")

    checkout_del_dir()
