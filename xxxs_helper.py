import pyautogui as pg
import time

qx = "qx.png"
qd = "qd.png"
pos = pg.locateOnScreen(ksxx)

def go(sleep_time):
    while True :
        time.sleep(sleep_time)
        pos = pg.locateOnScreen(qx)
        if (  pos is not None ):
            pg.click(pos[0] , pos[1])
        pos = pg.locateOnScreen(qd)
        if (  pos is not None ):
            pg.click(pos[0] , pos[1])



