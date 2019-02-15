import serial

class scaler_conection:

    def __init__(self, serialport):
        self.rawPort = serialport
        self.baud = 19200
        self.comandSetPower = {
            "Off" : "s power 0",
            "On" : "s power 1"
            }

        self.comandSetSource = {
            "CV" : "s source 0",
            "SV" : "s source 1",
            "COMP" : "s source 2",
            "PC" : "s source 3",
            "VGA" : "s source 3",
            "HDMI" : "s source 4"
            }

        self.comandSetOutput = {
            "NATIVE" : "s output 0",
            "VGA" : "s output 1",
            "SVGA" : "s output 2",
            "XGA" : "s output 3",
            "SXGA" : "s output 4",
            "UXGA" : "s output 5",
            "480I" : "s output 6",
            "480P" : "s output 7",
            "720P60" : "s output 8",
            "1080I60" : "s output 9",
            "1080P60" : "s output 10",
            "576I60" : "s output 11",
            "576P60" : "s output 12",
            "720P50" : "s output 13",
            "1080I50" : "s output 14",
            "1080P50" : "s output 15",
            "WXGA" : "s output 16",
            "WSXGA" : "s output 17",
            "WUXGA" : "s output 18",
            "WXGA+" : "s output 19"
            }

        self.comandSetSize = {
            "FULL" : "s size 0",
            "OVERSCAN" : "s size 1",
            "UNDERSCAN" : "s size 2",
            "LETTERBOX" : "s size 3",
            "PANSCAN" : "s size 4",
            "FOLLOW" : "s size 5"
            }



    def conect(self):
        #attempts to connect to scaler
        try:
            self.port = serial.Serial(self.rawPort, self.baud, timeout=1)
            return 0

        except:
            return 1

    def sendCommand(self, command):
        #encodes and sends command to scaler
        self.port.write(command.encode())

    def readRespone(self):
        #reads and decodes responce from scaler
        #returns responce
        responce = self.port.read(100).decode()
        return response


