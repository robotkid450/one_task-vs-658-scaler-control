import serial


class scaler_connection:

    def __init__(self, serialport):
        # Configure serial port.
        # The scaler has a fixed port set up of 19200 8N1.
        self.rawPort = serialport
        self.baud = 19200

        # Translation tables.
        self.commandSetPower = {
            "Off": "s power 0",
            "On": "s power 1"
            }

        self.commandSetSource = {
            "CV": "s source 0",
            "SV": "s source 1",
            "COMP": "s source 2",
            "PC": "s source 3",
            "VGA": "s source 3",
            "HDMI": "s source 4"
            }

        self.commandSetOutput = {
            "NATIVE": "s output 0",
            "VGA": "s output 1",
            "SVGA": "s output 2",
            "XGA": "s output 3",
            "SXGA": "s output 4",
            "UXGA": "s output 5",
            "480I": "s output 6",
            "480P": "s output 7",
            "720P60": "s output 8",
            "1080I60": "s output 9",
            "1080P60": "s output 10",
            "576I60": "s output 11",
            "576P60": "s output 12",
            "720P50": "s output 13",
            "1080I50": "s output 14",
            "1080P50": "s output 15",
            "WXGA": "s output 16",
            "WSXGA": "s output 17",
            "WUXGA": "s output 18",
            "WXGA+": "s output 19"
            }

        self.commandSetSize = {
            "FULL": "s size 0",
            "OVERSCAN": "s size 1",
            "UNDERSCAN": "s size 2",
            "LETTERBOX": "s size 3",
            "PANSCAN": "s size 4",
            "FOLLOW": "s size 5"
            }

        self.commandSetOSDNotice = {
            "INFO": "s osdnotice 0",
            "OFF": "s osdnotice 1",
            "ON": "s osdnotice 2"
            }

        self.commandSetPictureMode = {
            "STANDARD": "s picturemode 0",
            "MOVIE": "s picturemode 1",
            "VIVID": "s picturemode 1",
            "USER": "s picturemode 2"
            }

        self.commandSetAudioMute = {
            "OFF": "s audiomute 0",
            "ON": "s audiomute 1"
            }

        self.commandSetAudioDelay = {
            "OFF": "s audiodelay 0",
            "40MS": "s audiodelay 1",
            "110MS": "s audiodelay 2",
            "150MS": "s audiodelay 3"
            }

    def connect(self):
        # attempts to connect to scaler
        try:
            self.port = serial.Serial(self.rawPort, self.baud, timeout=1)
            return 0

        except:
            # will add actual error condition later,
            # when I can test with hardware.
            return 1

    def sendCommand(self, command):
        # encodes and sends command to scaler
        self.port.write(command.encode())

    def readRespone(self):
        # reads and decodes responce from scaler
        # returns responce
        responce = self.port.read(100).decode()
        return response
