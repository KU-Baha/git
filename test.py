import shutil

from commands.utils.config import BASE_FS_PATH

shutil.make_archive('test', 'zip', BASE_FS_PATH)
