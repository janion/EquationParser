'''
Created on 13 Jun 2016

@author: Janion
'''
import wx

class Window(wx.Frame):
    
    SIZE = 15
    
    def __init__(self, parent, idd, title):
        wx.Frame.__init__(self, parent, idd, title, size=(30 * (self.SIZE + 1), 30 * (self.SIZE + 2)))
        self.panel = wx.Panel(self, -1)
        self.SetMinSize(self.GetSize())
        
        self.btns = [[None for y in xrange(self.SIZE)] for x in xrange(self.SIZE)]
        
        for x in xrange(self.SIZE):
            for y in xrange(self.SIZE):
                self.btns[x][y] = wx.StaticText(self.panel, -1, '', pos=(10 + (30 * x), 10 + (30 * y)), size=(25, 25))
                self.btns[x][y].Enable(False)
                self.btns[x][y].SetBackgroundColour(wx.LIGHT_GREY)
    
    def setColour(self, position, red, green, blue):
        self.btns[position[0]][position[1]].SetBackgroundColour((red, green, blue))
        self.btns[position[0]][position[1]].Refresh()
    
    def setColourByString(self, command):
        xpos = 1
        ypos = command.index("y")
        x = int(command[xpos:ypos])
        
        if "GREY" in command:
            greypos = command.index("GREY")
            y = int(command[ypos + 1:greypos])
            colour = wx.LIGHT_GREY
        else:
            rpos = command.index("r")
            gpos = command.index("g")
            bpos = command.index("b")
            
            y = int(command[ypos + 1:rpos])
            red = int(command[rpos + 1:gpos])
            grn = int(command[gpos + 1:bpos])
            blu = int(command[bpos + 1:len(command)])
            
            colour = (red, grn, blu)
        
        self.btns[x][y].SetBackgroundColour(colour)
        self.btns[x][y].Refresh()
            
        