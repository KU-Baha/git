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


# Нужно переписать
def get_data_by_key(key: str, database: list) -> dict:
    for line in database:
        if key not in line:
            continue

        data = line.split(',')

        return {'file_hash': data[0], 'file_path': data[1]}

    return {}


def check_in_database(path: str, database: list):
    for line in database:
        lines = line.split('/')
        if path in line:
            if len(lines) == 2:

                if path == lines[1]:
                    return True

                continue

            return True

    return False


def add_to_database(new_file_hash: str, new_file_path: str, database: list) -> bool:
    if check_in_database(new_file_path, database):
        return False

    with open(DATABASE_PATH, 'w') as file:
        file.write('\n'.join(database))
        file.write(f"{new_file_hash}, /{new_file_path}\n")

    return True


def delete_from_database(file_hash: str, file_name: str, database: list) -> bool:
    if not get_data_by_key(file_hash, database):
        return False

    for i in range(len(database)):
        if file_hash not in database[i] or file_name not in database[i]:
            continue

        del database[i]

        with open(DATABASE_PATH, 'w') as file:
            file.write('\n'.join(database))

        return True

    return False
