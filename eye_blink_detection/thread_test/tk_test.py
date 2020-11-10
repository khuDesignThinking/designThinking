import eye_test
import test
from threading import Thread

t1 = Thread(target = test.test_1, args=())
t2 = Thread(target = eye_test.blink_detect, args=())

t1.start()
t2.start()