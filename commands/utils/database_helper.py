from hashlib import sha1

from commands.utils.fs_helper import check_file
from commands.utils.config import *


def hash_file(file_path: str) -> str:
    if not check_file(file_path):
        return ''

    with open(file_path, "rb") as file:
        return sha1(file.read()).hexdigest()


def database_list(inter_database_path=None) -> list:
    database_path = DATABASE_PATH

    if inter_database_path:
        database_path = inter_database_path

    if not check_file(database_path):
        return []

    with open(database_path, "r") as file:
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
        path_in_database_split = line[1].split('/')[1:]
        path_split = path.split('/')
        if path_in_database_split == path_split[:len(path_in_database_split)]:
            return index, line

        path_in_data = line[1].lstrip('/')
        new_path = path.lstrip('/')

        if new_path == path_in_data:
            return index, line

    return ()


def add_to_database(new_file_hash: str, new_file_path: str, database: list, inter_database_path: str = None) -> bool:
    database_path = DATABASE_PATH

    if inter_database_path:
        database_path = inter_database_path

    if check_in_database(new_file_path, database):
        return False

    with open(database_path, 'w') as file:
        file.write('\n'.join(database))
        file.write(f"{new_file_hash},/{new_file_path.lstrip('/')}\n")

    return True


def delete_from_database(file_path: str, database: list, inter_database_path: str = None) -> tuple:
    database_path = DATABASE_PATH

    if inter_database_path:
        database_path = inter_database_path

    data = check_in_database(file_path, database)

    if not data:
        return ()

    del database[data[0]]

    with open(database_path, 'w') as file:
        file.write('\n'.join(database))

    return data[1]


def get_path(database: list) -> list:
    paths = []

    for line in database:
        paths.append(line.split(',')[1])

    return paths
