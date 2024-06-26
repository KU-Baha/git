from commands.utils.database_helper import database_list, get_path
from commands.utils.config import LIST_FILE_PATH, LIST_FILE_NAME


def list_file(*args) -> None:
    if args:
        print("Command list doesn't take any arguments!")
        exit()

    with open(LIST_FILE_PATH, 'r') as file:
        print(file.read())


def get_tree_dict(paths: list) -> dict:
    tree = {}

    for path in paths:
        current_lvl = tree
        directories = path.split('/')

        for directory in directories:

            if directory not in current_lvl:
                current_lvl[directory] = {}

            current_lvl = current_lvl[directory]

    return tree


def to_tree(d, c=0):
    for a, b in d.items():
        yield '   '.join('|' for _ in range(c + 1)) + f'[{len(b)}]---{a}/' if b != {} \
            else '   '.join('|' for _ in range(c + 1)) + f'---{a}'
        yield from ([] if b is None else to_tree(b, c + 1))


def list_file_helper(base_dir=None) -> bool:
    list_path = LIST_FILE_PATH

    if base_dir:
        list_path = f"{base_dir}/{LIST_FILE_NAME}"

    database = database_list()[:-1]
    paths = get_path(database)
    nested_dict = get_tree_dict(paths)
    with open(list_path, 'w') as file:
        file.write('\n'.join(to_tree(nested_dict)))

    return True


if __name__ == '__main__':
    if not list_file_helper():
        exit(0)
    list_file()
