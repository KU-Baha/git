from commands.snapshot.snapshot_create import snapshot_create_helper
from commands.snapshot.snapshot_delete import snapshot_delete_helper
from commands.snapshot.snapshot_list import snapshot_list_helper
from commands.snapshot.snapshot_restore import snapshot_restore_helper

commands_list = {
    'create': snapshot_create_helper,
    'list': snapshot_list_helper,
    'delete': snapshot_delete_helper,
    'restore': snapshot_restore_helper
}
