from commands import add_file, init_fs, del_file, list_files
from commands.backup import backup_helper
from commands.checkout import checkout_helper
from commands.commit import commit_helper
from commands.restore import restore_helper
from commands.snapshot.snapshot_main import snapshot
from commands.snapshot import snapshot_commads


def help_command():
    print('Main commands: ')
    for i in commands_list:
        print(f"    - {i}")
    print('Snapshot commands: ')
    for i in snapshot_commads.commands_list:
        print(f"    - snapshot {i}")


commands_list = {
    'add': add_file.add_file_helper,
    'del': del_file.del_file_helper,
    'list': list_files.list_file,
    'init': init_fs.init_fs_helper,
    'backup': backup_helper,
    'restore': restore_helper,
    'snapshot': snapshot,
    'checkout': checkout_helper,
    'commit': commit_helper,
    'help': help_command
}
