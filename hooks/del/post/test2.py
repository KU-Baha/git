import sys
import time


def start():
    args = sys.argv
    print(f"Start post hook {args}")
    time.sleep(2)
    print(f"End post hook {args}")


start()
