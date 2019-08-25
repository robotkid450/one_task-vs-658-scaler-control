#!/usr/bin/env python
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
import Tkinter as tk
import tkMessageBox
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
        self.powerFrame.powerONButton['command'] = self.powerON
        self.powerFrame.powerONButton['text'] = "Power ON"
        self.powerFrame.powerONButton['fg'] = "green"
        self.powerFrame.powerONButton.grid(column=0, row=0)

        self.powerFrame.powerOFFButton = tk.Button(self.powerFrame)
        self.powerFrame.powerOFFButton['state'] = tk.DISABLED
        #self.powerFrame.powerOFFButton['command'] = self.powerOFF
        self.powerFrame.powerOFFButton['text'] = "Power OFF"
        self.powerFrame.powerOFFButton['fg'] = "red"
        self.powerFrame.powerOFFButton.grid(column=1, row=0)




        self.sourceFrame = tk.Frame(self.root)
        self.sourceFrame.grid(column=0, row=1)

        self.sourceFrame.labelName = tk.Label(self.sourceFrame, text="NOM")
        self.sourceFrame.labelName.grid(column=0, row=1)

        self.sourceFrame.mb = tk.Menubutton(self.sourceFrame, text="Source")
        self.sourceFrame.mb.grid(column=0, row=2)

        self.sourceFrame.mb.menu = tk.Menu(self.sourceFrame.mb)
        self.sourceFrame.mb['menu'] = self.sourceFrame.mb.menu
        self.sourceFrame.mb.menu.add_radiobutton(label='input 1')

        #self.sourceFrame.mb.menu.grid()




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
        return (tkMessageBox.askokcancel(Title, message))

    def powerON(self):
        confim = self._powerConf(0)
        if confim == True:
            print "true"
        else:
            print "false"


def main(args):
    app = Application()
    app.mainloop()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
