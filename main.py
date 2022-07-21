import sys
import time
from command import commands_list
from commands.utils.hook_helper import run_hooks


def main():
    argv = sys.argv

    if len(argv) <= 1:
        print("Write command!")
        exit()

    _, command, *args = argv

    if command not in commands_list:
        print("Command not found!")
        exit()

    run_hooks(command, 'pre')

    commands_list[command](*args)

    run_hooks(command, 'post')


if __name__ == '__main__':
    main()
