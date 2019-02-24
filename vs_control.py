import serial
import time


class scaler_connection:

    def __init__(self, serialport):
        # Configure serial port.
        # The scaler has a fixed port set up of 19200 8N1.
        self.rawPort = serialport
        self.baud = 19200

        self.serialConnected = 0

        # Translation tables.
        self.translationTableSet = {
            "power" : {
                "OFF": "s power 0",
                "0": "s power 0",
                "ON": "s power 1",
                "1": "s power 1"},
            "source" : {
                "CV": "s source 0",
                "YC": "s source 1",
                "COMP": "s source 2",
                "PC": "s source 3",
                "VGA": "s source 3",
                "HDMI": "s source 4" },
            "output" : {
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
                "WXGA+": "s output 19" },
            "size" : {
                "FULL": "s size 0",
                "OVERSCAN": "s size 1",
                "UNDERSCAN": "s size 2",
                "LETTERBOX": "s size 3",
                "PANSCAN": "s size 4",
                "FOLLOW": "s size 5" },
            "osd" : {
                "INFO": "s osdnotice 0",
                "OFF": "s osdnotice 1",
                "ON": "s osdnotice 2" },
            "mode" : {
                "STANDARD": "s picturemode 0",
                "MOVIE": "s picturemode 1",
                "VIVID": "s picturemode 1",
                "USER": "s picturemode 2" },
            "mute" : {
                "OFF": "s audiomute 0",
                "ON": "s audiomute 1" },
            "delay" : {
                "OFF": "s audiodelay 0",
                "40MS": "s audiodelay 1",
                "110MS": "s audiodelay 2",
                "150MS": "s audiodelay 3" },
            "nr" : {
                "OFF": "s nr 0",
                "LOW": "s nr 1",
                "MIDDLE": "s nr 2",
                "HIGH": "s nr 3" },
            "temp" : {
                "NORMAL": "s colortemp 0",
                "WARM": "s colortemp 1",
                "COOL": "s colortemp 2",
                "USER": "s colortemp 3" }
            }

        self.valueCommands = [ 'contrast', 'brightness', 'hue',
            'saturation', 'sharpness', 'pchposition', 'pcvposition',
            'pcclock', 'pchphase', 'red', 'green', 'blue', 'osdhposition',
            'osdvposition', 'osdtimeout', 'osdbackground' ]


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
            print "not connected"
            self._connect()
        command = command + '\r'
        # encodes and sends command to scaler
        print command
        self.port.write(command.encode())

    def _readline(self):
        time.sleep(.5)
        print self.port.inWaiting()
        msg = self.port.read(self.port.inWaiting() + 2)

        return msg

    def _readresponce(self):
        responceRaw = self._readline()
        responceRaw = responceRaw[2:-2]
        print "responceRaw"
        print responceRaw
        data = responceRaw.split(' ')
        return data

    def _getStatus(self, command):
        self._sendCommand("r " + command)
        output = self._readresponce()
        return output

    def _setCommandTable(self, command, option):
        command = str(command).lower()
        option = str(option).upper()
        if command in self.translationTableSet:
            if option in self.translationTableSet[command]:
                self._sendCommand(self.translationTableSet[command][option])
            else:
                # Create proper exception
                raise ValueError('invalid option')
        else:
            raise ValueError('invalid command')

        return self._readresponce()

    def _setCommandValue(self,command, value, lower=0, upper=100):
        if str(command).lower() in self.valueCommands:
            if self._limitCheck(value, lower, upper):
                self._sendCommand("s " + str(command).lower() + ' ' + str(value))
            else:
                raise ValueError("Value out of bounds.")
        else:
            raise ValueError("Invalid command")

        return self._readresponce()

    def _limitCheck(self, value, lower=0, upper=100):
        if value >= lower and value <= upper:
            return True
        else:
            return False

    def setPower(self, power):
        return self._setCommandTable('power', power)

    def setSource(self, source):
        return self._setCommandTable('source', source)

    def setOutput(self, output):
        return self._setCommandTable('output', output)

    def setSize(self, size):
        return self._setCommandTable('size', size)

    def setOSDNotice(self, osd):
        return self._setCommandTable('osd',osd )

    def setPictureMode(self, mode):
        return self._setCommandTable('mode', mode)

    def setAudioMute(self, mute):
        return self._setCommandTable('mute', mute)

    def setAudioDelay(self, delay):
        return self._setCommandTable('delay', delay)

    def setNR(self, nr):
        return self._setCommandTable('nr', nr)

    def setColorTemp(self, temp):
        return self._setCommandTable('temp', temp)

    def setContrast(self, contrast):
        return self._setCommandValue('contrast', contrast)

    def setBrightness(self, brightness):
        if self._limitCheck(brightness):
            return self._sendCommand("s brightness " + str(brightness))
        else:
            print("error value out of bounds")
            return -5

    def setHue(self, hue):
        if self._limitCheck(hue):
            return self._sendCommand("s hue " + str(hue))
        else:
            print("error value out of bounds")
            return -5

    def setSaturation(self, sat):
        if self._limitCheck(sat):
            return self._sendCommand("s saturation " + str(sat))
        else:
            print("error value out of bounds")
            return -5

    def setSharpness(self, sharp):
        if self._limitCheck(sharp):
            return self._sendCommand("s sharpness " + str(sharp))
        else:
            print("error value out of bounds")
            return -5

    def setPCHPosition(self, pch):
        if self._limitCheck(pch):
            return self._sendCommand("s pchposition " + str(pch))
        else:
            print("error value out of bounds")
            return -5

    def setPCVPosition(self, pcv):
        if self._limitCheck(pcv):
            return self._sendCommand("s pcvposition " + str(pcv))
        else:
            print("error value out of bounds")
            return -5

    def setPCClock(self, pcclock):
        if self._limitCheck(pcclock):
            return self._sendCommand("s pcclock " + str(pcclock))
        else:
            print("error value out of bounds")
            return -5

    def setPCPhase(self, pcphase):
        if self._limitCheck(pcphase, 0, 63):
            return self._sendCommand("s pchphase " + str(pcphase))
        else:
            print("error value out of bounds")
            return -5

    def setRed(self, red):
        if self._limitCheck(red):
            return self._sendCommand("s red " + str(red))
        else:
            print("error value out of bounds")
            return -5

    def setGreen(self, green):
        if self._limitCheck(green):
            return self._sendCommand("s green " + str(green))
        else:
            print("error value out of bounds")
            return -5

    def setBlue(self, blue):
        if self._limitCheck(blue):
            return self._sendCommand("s blue " + str(blue))
        else:
            print("error value out of bounds")
            return -5

    def setOSDHPosition(self, osdh):
        if self._limitCheck(osdh):
            return self._sendCommand("s osdhposition " + str(osdh))
        else:
            print("error value out of bounds")
            return -5

    def setOSDVPosition(self, osdv):
        if self._limitCheck(osdv):
            return self._sendCommand("s osdvposition " + str(osdv))
        else:
            print("error value out of bounds")
            return -5

    def setOSDTimeout(self, timeout):
        if self._limitCheck(timeout):
            return self._sendCommand("s osdtimeout " + str(timeout))
        else:
            print("error value out of bounds")
            return -5

    def setOSDBackground(self, osdbackground):
        if self._limitCheck(osdbackground, 0, 8):
            return self._sendCommand("s osdbackground " + str(osdbackground))
        else:
            print("error value out of bounds")
            return -5

    def setReset(self):
        return self._sendCommand("s reset 1")

    def getPower(self):
        self._sendCommand("r power")
        output = self._readresponce()
        return output


