from commands.utils.config import SNAPSHOTS_DB_PATH


def snapshot_list():
    with open(SNAPSHOTS_DB_PATH, 'r') as file:
        print(file.read())


def snapshot_list_helper(*args):
    if args:
        print("Command list doesn't take any arguments!")
        exit()

    snapshot_list()
