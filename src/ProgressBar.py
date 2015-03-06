import sys
import os

class ProgressBar:
    """
    Progress bar object
    This object is caracterized by a maximal value, the maximal value of the bar, and the title of the bar
    """
    def __init__ (self, valmax, maxbar, title):
        if valmax <= 0:  
            valmax = 1
        if maxbar <= 0:
            maxbar = 100
        if maxbar > 200: 
            maxbar = 200
        if title == "":
            title = "Progress bar"
        self.valmax = valmax
        self.maxbar = maxbar
        self.title  = title
    
    def update(self, val):
        """
        Method to update the ProgressBar object
        """
        if val > self.valmax:
            val = self.valmax
        
        perc  = round((float(val) / float(self.valmax)) * 100)
        scale = 100.0 / float(self.maxbar)
        bar   = int(perc / scale)
  
        print("{0} [{1}>{2}] {3}%".format(self.title, '=' * bar, ' ' * (self.maxbar - bar), perc), end="\r")