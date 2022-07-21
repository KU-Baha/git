from commands import add_file, init_fs, del_file, list_files
from commands.backup import backup_helper
from commands.restore import restore_helper
from commands.utils.hook_helper import create_hook_structure

commands_list = {
    'add': add_file.add_file_helper,
    'del': del_file.del_file_helper,
    'list': list_files.list_file,
    'init': init_fs.init_fs_helper,
    'hook': create_hook_structure,
    'backup': backup_helper,
    'restore': restore_helper
}
