from commands.utils.database_helper import database_list, get_path


def get_tree_dict(paths):
    tree = {}

    for path in paths:
        current_lvl = tree

        for i in path.split('/'):

            if i not in current_lvl:
                current_lvl[i] = {}

            current_lvl = current_lvl[i]

    return tree


def beautiful_print(t, s):
    if not isinstance(t, dict) and not isinstance(t, list):
        print("--" * s + str(t))
    else:
        for key in t:
            print("---" * s + str(key))
            if not isinstance(t, list):
                beautiful_print(t[key], s + 1)


def list_file():
    database = database_list()[:-1]
    paths = get_path(database)
    nested_dict = get_tree_dict(paths)
    beautiful_print(nested_dict, 1)


if __name__ == '__main__':
    list_file()
