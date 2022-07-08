import os
import subprocess
from pathlib import Path


def create_hook_structure(called_path: Path) -> None:
    commands_list = ['add', 'del', 'list', 'init']
    hooks_list = ['pre', 'post']

    for command in commands_list:
        path = called_path / 'hooks' / command
        path.mkdir(parents=True, exist_ok=True)

        for hook in hooks_list:
            hook_path = path / hook
            hook_path.mkdir(parents=True, exist_ok=True)


def hook_helper() -> None:
    called_path = Path(os.getcwd())
    create_hook_structure(called_path)


def run_hooks(state: str, command: str) -> None:
    hooks = os.listdir(f'hooks/{command}/{state}/')
    for hook in sorted(hooks):
        if Path(f'hooks/{command}/{state}/{hook}').is_file():
            subprocess.Popen(f'python hooks/{command}/{state}/{hook}', shell=True)
