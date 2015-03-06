import ProgressBar
import time

def testPB(valmax, maxbar, title):
    i = 1
    barTest = ProgressBar.ProgressBar(valmax, maxbar, title)
    for _ in range(valmax):
        barTest.update(i)
        time.sleep(0.50)
        i = i+1