# from commands.del_file import del_file_helper
# from commands.restore import restore
# from commands.utils.config import SNAPSHOT_DIR_PATH, INTERMEDIATE_DIR, COMMIT_DIR, INTERMEDIATE_DATABASE
# from commands.utils.database_helper import database_list, delete_from_database
# from commands.utils.fs_helper import check_file, get_file_in_snapshot, del_intermediate_dir
#
#
# def commit_helper(*args) -> None:
#     if len(args) != 3:
#         print("Command 'commit' takes 3 arguments - snapshot, file_path, file_in_snapshot")
#         return
#
#     snapshot, file_path, file_in_snapshot = args
#
#     snapshot_path = f'{SNAPSHOT_DIR_PATH}/{snapshot}.zip'
#
#     if not check_file(snapshot_path):
#         print("Snapshot not found!")
#         return
#
#     if not check_file(file_path):
#         print("File not found!")
#         return
#
#     restore(snapshot_path, INTERMEDIATE_DIR)
#
#     database = database_list(INTERMEDIATE_DATABASE)
#
#     if not delete_from_database(file_in_snapshot, database):
#         print("File not found in snapshot!")
#         del_intermediate_dir()
#         return
#
#     del_file_helper(file_in_snapshot, database_path=INTERMEDIATE_DATABASE)
