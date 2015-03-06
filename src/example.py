import ProgressBar
import time

def testPB(valmax, maxbar, title, pacman_style = False):
    i = 1
    barTest = ProgressBar.ProgressBar(valmax, maxbar, title, pacman_style)
    for _ in range(valmax):
        barTest.update(i)
        time.sleep(0.50)
        i = i+1