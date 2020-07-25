#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  main.py
#
#  Copyright 2019 Josh <robotkid450@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#


#from Tkinter import *
import tkinter as tk
import tkinter.messagebox
import vs_control as vsc

class Application(tk.Frame):
    def __init__(self, master=None):
        self.connected = False

        self.root = tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.powerFrame = tk.Frame(self.root)
        self.powerFrame.grid(column=0, row=0)

        self.powerFrame.powerONButton = tk.Button(self.powerFrame)
        self.powerFrame.powerONButton['state'] = tk.DISABLED
        #self.powerFrame.powerONButton['command'] = self.powerON
        self.powerFrame.powerONButton['text'] = "Power ON"
        self.powerFrame.powerONButton['fg'] = "green"
        self.powerFrame.powerONButton.grid(column=0, row=0)

        self.powerFrame.powerOFFButton = tk.Button(self.powerFrame)
        self.powerFrame.powerOFFButton['state'] = tk.DISABLED
        #self.powerFrame.powerOFFButton['command'] = self.powerOFF
        self.powerFrame.powerOFFButton['text'] = "Power OFF"
        self.powerFrame.powerOFFButton['fg'] = "red"
        self.powerFrame.powerOFFButton.grid(column=1, row=0)



        #create input control frame
        self.inputCtlFrame = tk.Frame(self.root)
        self.inputCtlFrame.grid(column=0, row=1)
        
        #create source menu
        self.inputCtlFrame.MbSource = tk.Menubutton(self.inputCtlFrame, text="Source")
        self.inputCtlFrame.MbSource.grid(column=0, row=1)

        self.inputCtlFrame.MbSource.menu = tk.Menu(self.inputCtlFrame.MbSource)
        self.inputCtlFrame.MbSource['menu_source'] = self.inputCtlFrame.MbSource.menu
        self.sourceVar = tk.StringVar()
        self.inputCtlFrame.MbSource.menu.add_radiobutton(label='CV', variable=self.sourceVar, value='CV')
        self.inputCtlFrame.MbSource.menu.add_radiobutton(label='YC', variable=self.sourceVar, value='YC')
        self.inputCtlFrame.MbSource.menu.add_radiobutton(label='YPbPr', variable=self.sourceVar, value='YPbPr')
        self.inputCtlFrame.MbSource.menu.add_radiobutton(label='RGB', variable=self.sourceVar, value='RGB')
        self.inputCtlFrame.MbSource.menu.add_radiobutton(label='HDMI', variable=self.sourceVar, value='HDMI')
        
        
        

    #def _


    def _connectSerial(self, port):
        return 0

    def _powerConf(self, state):
        message = "Are you sure?"
        if state == 0:
            Title = "Power OFF?"
        elif state == 1:
            Title = "Power ON?"
        else:
            return -1
        return (tkinter.messagebox.askokcancel(Title, message))

    def powerON(self):
        confim = self._powerConf(0)
        if confim == True:
            print("true")
        else:
            print("false")


def main(args):
    app = Application()
    app.mainloop()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
