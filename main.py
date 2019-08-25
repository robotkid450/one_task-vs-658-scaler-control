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


from Tkinter import *
import tkMessageBox
import vs_control as vsc

class Application(Frame):
    def __init__(self, master=None):
        self.connected = False

        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.powerONButton = Button(self)
        #self.
        self.powerONButton['command'] = self.powerON
        self.powerONButton['text'] = "Power ON"
        self.powerONButton['fg'] = "green"
        self.powerONButton.pack({"side": "left"})



    def _connectSerial(self, port):
        return 0
        #vsc.

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
    root = Tk()
    app = Application(master=root)
    app.mainloop()
    root.destroy()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
