import vs_control as vsc
import time

a = vsc.scaler_connection('/dev/ttyUSB0')
a._connect()

print "power"

a.setPower("off")

time.sleep(1)

a.setPower("on")

time.sleep(1)
print "source"

a.setSource('HDMI')

time.sleep(1)
print "output"

a.setOutput('VGA')

time.sleep(1)
print "size"

a.setSize('FULL')

time.sleep(1)
print "osd"

a.setOSDNotice('ON')


time.sleep(1)
print "picmode"

a.setPictureMode('USER')

time.sleep(1)
print "mute"

a.setAudioMute('ON')

time.sleep(1)
print "delay"

a.setAudioDelay("OFF")

time.sleep(1)
print "nr"
a.setNR('LOW')

time.sleep(1)
print "ccol temp"
a.setColorTemp("WARM")

time.sleep(1)
print "cont"
a.setContrast(5)

time.sleep(1)
print "bright"
a.setBrightness(5)

time.sleep(1)
print "hue"
a.setHue(5)

time.sleep(1)
print "sat"
a.setSaturation(4)

time.sleep(1)
print "sharp"
a.setSharpness(5)

time.sleep(1)
print "pchp"
a.setPCHPosition(6)

time.sleep(1)
print "pcvp"
a.setPCVPosition(6)

time.sleep(1)
print "pcclock"
a.setPCClock(6)

time.sleep(1)
print "pcphase"
a.setPCPhase(6)

time.sleep(1)
print "red"
a.setRed(1)

time.sleep(1)
print "green"
a.setGreen(1)

time.sleep(1)
print "blue"
a.setBlue(9)

time.sleep(1)
print "osdhpos"
a.setOSDHPosition(23)

time.sleep(1)
print "osdvpos"
a.setOSDVPosition(12)

time.sleep(1)
print "osdtime"
a.setOSDTimeout(6)

time.sleep(1)
print "osdback"
a.setOSDTimeout(70)

#print "reset"
#a.setReset()
