import sys
from command import commands_list
from commands.utils.fs_helper import check_inited
from commands.utils.hook_helper import run_hooks


def main():
    argv = sys.argv

    if len(argv) <= 1:
        print("Write command! \nIf you don't know commands you can write command 'help'")
        return

    _, command, *args = argv

    if command not in commands_list:
        print("Command not found! \nIf you don't know commands you can write command 'help'")
        return

    if not check_inited() and command != 'init':
        print('FS not initialized!')
        return

    run_hooks(command, 'pre')

    commands_list[command](*args)

    run_hooks(command, 'post')


if __name__ == '__main__':
    main()
