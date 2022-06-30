from commands import add_file, init_fs, del_file

commands_list = {
    'init': init_fs.init_fs_helper,
    # 'list': file_list,
    'add': add_file.add_file_helper,
    'del': del_file.del_file_helper
}
