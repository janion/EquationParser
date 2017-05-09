'''
Created on 8 Apr 2016

@author: Janion
'''

import wx
import time
from FlatTestArray import Window
from threading import Thread
from EquationParser import Equation
        
################################################################################

def displayFunction(window, functionText):
    function = Equation(functionText)
    start = time.time()
    exitThread = False
    
    while True:
        now = time.time()
        for x in xrange(window.SIZE):
            for y in xrange(window.SIZE):
                val = function.evaluate(x, y, now - start)
                try:
                    window.IsActive()
                    if len(val) > 0:
#                         wx.CallAfter(window.setColour, [x, y], 0, 127 * val[0], 0)
                        val = 127 * val[0]
                        wx.CallAfter(window.setColour, [x, y], 0, val, 255 - val)
                    else:
                        wx.CallAfter(window.setColour, [x, y], 0, 0, 0)
                except:
                    exitThread = True
                    break
            if exitThread:
                break
        
        if not exitThread:
            time.sleep(0.1)
        
################################################################################

if __name__ == '__main__':
    app = wx.App()
    
    # # Folding lines?
    # function = "sin(t + ((x - 5) + (t * (y - 5)))) + 1"
    # Outward propagating sine rings
    function = "sin(sqrt(((x - 4.5) * (x - 4.5)) + ((y - 4.5) * (y - 4.5))) - (4 * t)) + 1"
#     # Oscillating sine rings
#     function = "sin(sqrt(((x - 4.5) * (x - 4.5)) + ((y - 4.5) * (y - 4.5))) - (2 * sin(t))) + 1"
#     # Diagonal moving waves
#     function = "sin(((x - 4.5) + (y - 4.5)) - (8 * t)) + 1"
#     # Spinning lines
#     function = "sin(((x - 4.5) * sin(t)) + ((y - 4.5) * cos(t))) + 1"

    # Create a window
    window = Window(None, -1, function)
    window.Show()

    workThread = Thread(target = displayFunction, args=(window, function) )
    workThread.start()
    
    app.MainLoop()