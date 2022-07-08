import sys
import time


def start():
    args = sys.argv
    print(f"Start pre hook {args}")
    time.sleep(2)
    print(f"End pre hook {args}")

start()
