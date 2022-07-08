from commands import add_file, init_fs, del_file, list_files
from commands.utils.hook_helper import hook_helper

commands_list = {
    'add': add_file.add_file_helper,
    'del': del_file.del_file_helper,
    'list': list_files.list_file,
    'init': init_fs.init_fs_helper,
    'plugin': hook_helper,
}
