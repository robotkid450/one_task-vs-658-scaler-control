import serial

class scaller_conection:

    def __init__(self, serialport):
        self.rawPort = serialport
        self.baud = 19200
        self.commandSetPower = {
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



    def conect(self)
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


