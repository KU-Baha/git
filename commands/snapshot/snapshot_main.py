from commands.snapshot.snapshot_commads import commands_list


def snapshot(*args):
    if len(args) <= 0:
        print('Write snapshot command!')
        return

    command, *args = args

    if command not in commands_list:
        print("Snapshot command not found! - Write command 'help'")
        return

    commands_list[command](*args)
