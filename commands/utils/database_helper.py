from hashlib import sha1

from .fs_helper import check_file
from .config import *


def hash_file(file_path: str) -> str:
    if not check_file(file_path):
        return ''

    with open(file_path, "rb") as file:
        return sha1(file.read()).hexdigest()


def database_list() -> list:
    if not check_file(DATABASE_PATH):
        return []

    with open(DATABASE_PATH, "r") as file:
        return file.read().split('\n')


def get_data_by_key(key: str, database: list) -> dict:
    for line in database:
        if key not in line:
            continue

        data = line.split(',')

        if check_in_database(data[1], database):
            return {'file_hash': data[0], 'file_path': data[1]}

        continue

    return {}


def check_in_database(path: str, database: list) -> tuple:
    for index, line in enumerate(database[:-1]):
        line = line.split(',')
        path_in_data = line[1].lstrip('/')
        new_path = path.lstrip('/')
        if new_path == path_in_data:
            return index, line

    return ()


def add_to_database(new_file_hash: str, new_file_path: str, database: list) -> bool:
    if check_in_database(new_file_path, database):
        return False

    with open(DATABASE_PATH, 'w') as file:
        file.write('\n'.join(database))
        file.write(f"{new_file_hash},/{new_file_path.lstrip('/')}\n")

    return True


def delete_from_database(file_path: str, database: list) -> tuple:
    data = check_in_database(file_path, database)

    if not data:
        return ()

    del database[data[0]]

    with open(DATABASE_PATH, 'w') as file:
        file.write('\n'.join(database))

    return data[1]


def get_path(database: list) -> list:
    paths = []

    for line in database:
        paths.append(line.split(',')[1])

    return paths
