import serial

class scaller_conection:

    def __init__(self, serialport):
        self.rawPort = serialport
        self.baud = 19200

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


