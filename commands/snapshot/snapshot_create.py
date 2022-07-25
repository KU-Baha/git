from pathlib import Path

from commands.snapshot.snapshot_db import snapshot_add_to_db, snapshot_get_database
from commands.snapshot.snapshot_helper import del_intermediate_dir, move_to_intermediate_dir, \
    move_back_from_intermediate_dir
from commands.utils.config import *
import shutil
import hashlib
from datetime import datetime, timezone


def snapshot_create(name: str, date: str) -> str:
    form = f'{name}-{date}'.encode()
    snapshot_hash = hashlib.md5(form).hexdigest()
    shutil.make_archive(f"{SNAPSHOT_DIR_IN_INTERMEDIATE_DIR}/{snapshot_hash}", 'zip', BASE_FS_PATH)
    return snapshot_hash


def snapshot_create_helper(*args) -> bool:
    if len(args) != 1:
        print("Command 'snapshot create' take one argument! - 'name' argument!")
        return False

    name = args[0]
    date = datetime.now(timezone.utc).strftime('%d.%m.%Y %H:%M')

    database = snapshot_get_database()

    if Path(SNAPSHOT_INTERMEDIATE_DIR).is_dir():
        del_intermediate_dir()

    move_to_intermediate_dir()

    snapshot_hash = snapshot_create(name, date)

    move_back_from_intermediate_dir()

    snapshot_add_to_db(name, date, snapshot_hash, database)

    del_intermediate_dir()

    print('Snapshot success created!')

    return True
