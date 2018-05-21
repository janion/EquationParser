'''
Created on 13 Jun 2016

@author: Janion
'''
import wx

class Window(wx.Frame):
    
    SIZE = 10
    
    def __init__(self, parent, idd, title):
        wx.Frame.__init__(self, parent, idd, title, size=(30 * (self.SIZE + 1), 30 * (self.SIZE + 2)))
        self.panel = wx.Panel(self, -1)
        self.SetMinSize(self.GetSize())
        
        self.btns = [[None for y in range(self.SIZE)] for x in range(self.SIZE)]
        
        for x in range(self.SIZE):
            for y in range(self.SIZE):
                self.btns[x][y] = wx.StaticText(self.panel, -1, '', pos=(10 + (30 * x), 10 + (30 * y)), size=(25, 25))
                self.btns[x][y].Enable(False)
                self.btns[x][y].SetBackgroundColour(wx.LIGHT_GREY)
    
    def setColour(self, position, red, green, blue):
        self.btns[position[0]][position[1]].SetBackgroundColour((red, green, blue))
