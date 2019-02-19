import serial


class scaler_connection:

    def __init__(self, serialport):
        # Configure serial port.
        # The scaler has a fixed port set up of 19200 8N1.
        self.rawPort = serialport
        self.baud = 19200

        self.serialConnecred = 0

        # Translation tables.
        self.commandSetPower = {
            "off": "s power 0",
            "Off": "s power 0",
            "OFF": "s power 0",
            "0": "s power 0",
            0: "s power 0",
            "on": "s power 1",
            "On": "s power 1",
            "ON": "s power 1",
            "1": "s power 1",
            1: "s power 1"
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

        self.commandSetNR = {
            "OFF": "s nr 0",
            "LOW": "s nr 1",
            "MIDDLE": "s nr 2",
            "HIGH": "s nr 3"
            }

        self.commandSetColorTemp = {
            "NORMAL": "s colortemp 0",
            "WARM": "s colortemp 1",
            "COOL": "s colortemp 2",
            "USER": "s colortemp 3"
            }

    def _connect(self):
        # attempts to connect to scaler
        try:
            self.port = serial.Serial(self.rawPort, self.baud, timeout=1)

        except:
            # will add actual error condition later,
            # when I can test with hardware.
            self.serialConnected = -1
            print("error connecting to device")

        else:
            self.serialConnected = 1

    def _disconnect(self):
        # disconects serial port
        if self.serialConnected != 1:
            return
        try:
            self.port.close()
        except:
            self.serialConnected = -1
            print("error disconecting ??")
        else:
            print("serial disconected")
            self.serialConnected = 0

    def _sendCommand(self, command):
        if self.serialConnected != 1:
            self._connect()
        command = command + '/r'
        # encodes and sends command to scaler
        print command
        self.port.write(command.encode())

    def _readline(self):
        # reads from input buffer until it reaches '\r' (carage return)
        msg = ''
        charsAvalible = self.port.in_waiting
        for num in range(charsAvalible):
            char = self.port.read().decode()
            if char != '\x0D':
                msg = msg + char
            else:
                break

        return msg

    def setPower(self, power):
        if power in self.commandSetPower:
            return self._sendCommand(self.commandSetPower[str(power)])
        else:
            print "invalid command "

    def setSource(self, source):
        if source in self.commandSetSource:
            return self._sendCommand(self.commandSetSource[str(source)])
        else:
            print "invalid command "

    def setOutput(self, output):
        if output in self.commandSetOutput:
            return self._sendCommand(self.commandSetOutput[str(output)])
        else:
            print "invalid command "

    def setSize(self, size):
        if size in self.commandSetSize:
            return self._sendCommand(self.commandSetSize[str(size)])
        else:
            print "invalid command "

    def setOSDNotice(self, notice):
        if notice in self.commandSetOSDNotice:
            return self._sendCommand(self.commandSetOSDNotice[str(notice)])
        else:
            print "invalid command "

    def setPictureMode(self, mode):
        if mode in self.commandSetPictureMode:
            return self._sendCommand(self.commandSetPictureMode[str(mode)])
        else:
            print "invalid command "

    def setAudioMute(self, mute):
        if mute in self.commandSetAudioMute:
            return self._sendCommand(self.commandSetAudioMute[str(mute)])
        else:
            print "invalid command "

    def setAudioDelay(self, delay):
        if delay in self.commandSetAudioDelay:
            return self._sendCommand(self.commandSetAudioDelay[str(delay)])
        else:
            print "invalid command "

    def setNR(self, nr):
        if nr in self.commandSetNR:
            return self._sendCommand(self.commandSetNR[str(nr)])
        else:
            print "invalid command "

    def setColorTemp(self, ct):
        if ct in self.commandSetColorTemp:
            return self._sendCommand(self.commandSetColorTemp[str(ct)])
        else:
            print "invalid command "

    def setContrast(self, contrast):
        return self._sendCommand("s contrast " + str(contrast))

    def setBrightness(self, brightness):
        return self._sendCommand("s brightness " + str(brightness))

    def setHue(self, hue):
        return self._sendCommand("s hue " + str(hue))

    def setSaturation(self, sat):
        return self._sendCommand("s saturation " + str(sat))

    def setSharpness(self, sharp):
        return self._sendCommand("s sharpness " + str(sharp))

    def setPCHPosition(self, pch):
        return self._sendCommand("s pchposition " + str(pch))

    def setPCVPosition(self, pcv):
        return self._sendCommand("s pcvposition " + str(pcv))

    def setPCClock(self, pcclock):
        return self._sendCommand("s pcclock " + str(pcclock))

    def setPCPhase(self, pcphase):
        return self._sendCommand("s pchphase " + str(pcphase))

    def setRed(self, red):
        return self._sendCommand("s red " + str(red))

    def setGreen(self, green):
        return self._sendCommand("s green " + str(green))

    def setBlue(self, blue):
        return self._sendCommand("s blue " + str(blue))

    def setOSDHPosition(self, osdh):
        return self._sendCommand("s osdhposition " + str(osdh))

    def setOSDVPosition(self, osdv):
        return self._sendCommand("s osdvposition " + str(osdv))

    def setOSDTimeout(self, timeout):
        return self._sendCommand("s osdtimeout " + str(timeout))

    def setOSDBackground(self, osdbackground):
        return self._sendCommand("s osdbackground " + str(osdbackground))

    def setReset(self):
        return self._sendCommand("s reset 1")
