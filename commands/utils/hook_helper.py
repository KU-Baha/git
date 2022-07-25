import os
import subprocess
import threading

from pathlib import Path

from commands.utils.config import HOOKS_PATH
from commands.utils.fs_helper import check_inited

commands_list = ['add', 'del', 'list', 'init']
hooks_list = ['pre', 'post']


def create_hook_structure() -> None:
    called_path = Path(os.getcwd())

    for command in commands_list:
        path = called_path / HOOKS_PATH / command
        path.mkdir(parents=True, exist_ok=True)

        for hook in hooks_list:
            hook_path = path / hook
            hook_path.mkdir(parents=True, exist_ok=True)


def run_hook(command, state, hook):
    try:
        subprocess.Popen(f'python {HOOKS_PATH}/{command}/{state}/{hook}', shell=True)
    except subprocess.STD_ERROR_HANDLE:
        exit()


def sort_hooks(hooks):
    new_hooks = []

    continue_index_list = []

    for index, hook in enumerate(hooks):

        if index in continue_index_list:
            continue

        if hook[0] != '@':
            new_hooks.append(hook)
            continue

        n_hook_list = [hook]

        children_start = index + 1

        for children_index, children_hook in enumerate(hooks[children_start:]):
            if children_hook[0] != '@':
                break

            n_hook_list.append(children_hook)
            continue_index_list.append(children_start + children_index)
            continue

        new_hooks.append(n_hook_list)

    return new_hooks


def wait_for(threads):
    for t in threads:
        t.join()


def run_hooks(command: str, state: str) -> None:
    if command not in commands_list:
        return

    if not check_inited():
        return

    if not Path(HOOKS_PATH).is_dir():
        print("Hooks structure doesn't found!")
        return

    hooks = os.listdir(f'{HOOKS_PATH}/{command}/{state}/')

    sorted_list = list(sorted(hooks, key=lambda x: x[1]))

    new_hooks = sort_hooks(sorted_list)

    for hook in new_hooks:
        if not isinstance(hook, list):
            thr = threading.Thread(target=run_hook, args=(command, state, hook),
                                   name=f'thr-{hook}', daemon=True)
            thr.start()
            thr.join()

            continue

        threads_list = []

        for sub_hook in hook:
            thr = threading.Thread(target=run_hook, args=(command, state, sub_hook),
                                   name=f'thr-{sub_hook}', daemon=True)
            threads_list.append(thr)
            thr.start()

        wait_for(threads_list)
