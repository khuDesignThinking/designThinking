import variable as v
import time

def test_1():
    while True:
        time.sleep(9)
        if v.cnt_blink >= 10:
            print("bliiiink")