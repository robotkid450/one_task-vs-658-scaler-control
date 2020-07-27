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


import tkinter as tk
import tkinter.messagebox
import vs_control as vsc


device='/dev/ttyUSB0'

class Application(tk.Frame):
    def __init__(self, master=None):
        self.connected = False
        
        self.sc = vsc.scaler_connection(serialport=device)
        
        self._connectSerial()

        self.root = tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self._createPower()
        
        self._createIOMenus()

    def _createPower(self):
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
        
    def _createIOMenus(self):
        #create input control frame
        self.inputCtlFrame = tk.Frame(self.root)
        self.inputCtlFrame.grid(column=0, row=1)
        

        self._createMenuSource()
        self._createMenuResolution()
        self._createMenuScaling()
        
    def _createMenuSource(self):        
        #create source menu
        self.sourceVar = tk.StringVar()
        self.inputCtlFrame.MbSource = tk.Menubutton(self.inputCtlFrame, text="Source")
        self.inputCtlFrame.MbSource.grid(column=0, row=1)

        self.inputCtlFrame.MbSource.menu = tk.Menu(self.inputCtlFrame.MbSource)
        self.inputCtlFrame.MbSource['menu'] = self.inputCtlFrame.MbSource.menu
        
        
        #create source menu items
        for item in self.sc.translationTableSet["source"]:
            self.inputCtlFrame.MbSource.menu.add_radiobutton(label=item, variable=self.sourceVar, value=item, command=self.setSource)
        
        try:
            source = self.sc.getSource()
            self.sourceVar.set(source)
        except:
            pass
        
            
    def _createMenuResolution(self):
        #create Resolution menu
        self.inputCtlFrame.MbResolution = tk.Menubutton(self.inputCtlFrame, text="Resolution")
        self.inputCtlFrame.MbResolution.grid(column=1, row=1)
        
        self.inputCtlFrame.MbResolution.menu = tk.Menu(self.inputCtlFrame.MbResolution)
        self.inputCtlFrame.MbResolution['menu'] = self.inputCtlFrame.MbResolution.menu
        
        self.resolutionVar = tk.StringVar()
        
        #create Resolution menu items
        for item in self.sc.translationTableSet["output"]:
            self.inputCtlFrame.MbResolution.menu.add_radiobutton(label=item, variable=self.resolutionVar, value=item, command=self.setResolution)
            
        try:
            resolution = self.sc.getOutput()
            self.resolutionVar.set(resolution)
        except:
            pass
        

    def _createMenuScaling(self):
        #create scaling menu
        self.inputCtlFrame.MbSize = tk.Menubutton(self.inputCtlFrame, text="Scaling Mode")
        self.inputCtlFrame.MbSize.grid(column=2, row=1)
        
        self.inputCtlFrame.MbSize.menu = tk.Menu(self.inputCtlFrame.MbSize)
        self.inputCtlFrame.MbSize['menu'] = self.inputCtlFrame.MbSize.menu
        
        self.sizeVar = tk.StringVar()
        
        #create scaling menu items
        for item in self.sc.translationTableSet["size"]:
            self.inputCtlFrame.MbSize.menu.add_radiobutton(label=item, variable=self.sizeVar, value=item, command=self.setSize)
            
            
        try:
            scaling = self.sc.getSize()
            self.sizeVar.set(scaling)
        except:
            pass


    def _connectSerial(self, port=device):
        self.sc.setPort(port)
        self.sc._connect()
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
            
    def setSource(self):
        print('set source')
        print(self.sourceVar.get())
        self.sc.setSource(self.sourceVar.get())
        return 0
    
    def setResolution(self):
        print('set resolution')
        print(self.resolutionVar.get())
        self.sc.setOutput(self.resolutionVar.get())
        return 0
    
    def setSize(self):
        print('set size')
        print(self.sizeVar.get())
        self.sc.setSize(self.sizeVar.get())
        return 0


def main(args):
    app = Application()
    app.mainloop()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
