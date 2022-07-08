import os
from pathlib import Path


def create_hook_structure(called_path: Path):
    commands_list = ['add', 'del', 'list', 'init']
    hooks_list = ['pre-hook', 'post-hook']

    for command in commands_list:
        path = called_path / 'hooks' / command
        path.mkdir(parents=True, exist_ok=True)

        for hook in hooks_list:
            hook_path = path / hook
            hook_path.mkdir(parents=True, exist_ok=True)


def hook_helper():
    called_path = Path(os.getcwd())
    create_hook_structure(called_path)
