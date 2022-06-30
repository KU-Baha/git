import os
import sys
from command import commands_list
# from helper.helper import check_init


def main():
    argv = sys.argv

    if len(argv) <= 1:
        print("Write command!")
        exit(0)

    _, command, *args = argv

    if command not in commands_list:
        print("Command not found!")
        exit(0)

    commands_list[command](*args)


if __name__ == '__main__':
    main()
