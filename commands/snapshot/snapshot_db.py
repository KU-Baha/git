from pathlib import Path

from commands.utils.config import SNAPSHOTS_DB_PATH


def snapshot_get_database() -> list:
    if not Path(SNAPSHOTS_DB_PATH).is_file():
        return []

    with open(SNAPSHOTS_DB_PATH, "r") as file:
        return file.read().split('\n')


def snapshot_check_in_db(snapshot_hash: str, database: list) -> tuple:
    for index, line in enumerate(database):
        if not line:
            continue

        snapshot_hash_in_db = line.split(',')[2]

        if snapshot_hash == snapshot_hash_in_db:
            return index, line
    return ()


def snapshot_add_to_db(name: str, date: str, snapshot_hash: str, database: list) -> bool:
    if snapshot_check_in_db(snapshot_hash, database):
        return False

    with open(SNAPSHOTS_DB_PATH, 'w') as file:
        file.write('\n'.join(database))
        file.write(f'{name},{date},{snapshot_hash}\n')

    return True


def snapshot_delete_from_db(snapshot_hash: str, database: list):
    data = snapshot_check_in_db(snapshot_hash, database)

    if not data:
        return ()

    del database[data[0]]

    with open(SNAPSHOTS_DB_PATH, 'w') as file:
        file.write('\n'.join(database))

    return data[1]
