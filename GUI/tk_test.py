import GUI_main
import CntBlinkAddFile as CBF
from threading import Thread

t1 = Thread(target = GUI_main.main, args=())
t2 = Thread(target = CBF.main, args=())

t1.start()
t2.start()