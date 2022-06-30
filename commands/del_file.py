# import os
# import sys
#
#
# # from helper.helper import del_file
#
#
# def del_file(dir_path, *args) -> bool:
#
#     file_path = f"{dir_path}/{BASE_FS_PATH}/{args[0]}"
#     database = database_list()
#     data = get_data_by_key(file_path, database)
#
#     if not data:
#         print("File not found!")
#         return False
#
#     file_name = data.get('file_name')
#     file_hash = data.get('file_hash')
#
#     if not check_file(file_path):
#         if not Path(file_path).is_dir():
#             print("File not found!")
#             return False
#
#         shutil.rmtree(Path(file_path), ignore_errors=True)
#         print("The directory has been deleted")
#         return True
#
#     if not delete_from_database(file_hash, file_name, database):
#         print("File not found in database!")
#         return False
#
#     os.remove(file_path)
#     print("The file has been deleted")
#     return True
#
#
# def del_file_helper(*args):
#     if len(args) != 1:
#         print("Command 'del' take 1 argument - file path!")
#         return False
#
#
# if __name__ == '__main__':
#     main()
