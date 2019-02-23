import vs_control as vsc

a = vsc.scaler_connection('a')

print "power"
a.setPower(1)
a.setPower("1")
a.setPower("on")
a.setPower("On")
a.setPower("ON")

a.setPower(0)
a.setPower("0")
a.setPower("off")
a.setPower("Off")
a.setPower("OFF")

a.setPower('asdsdfasdf')
a.setPower(134123412354314651354234)
print "source"

a.setSource('HDMI')
a.setSource("a")
a.setSource(0)

print "output"

a.setOutput('VGA')
a.setOutput('asd')
a.setOutput(0)

print "size"

a.setSize('FULL')
a.setSize('da')
a.setSize(0)

print "osd"

a.setOSDNotice('ON')
a.setOSDNotice('asdf')
a.setOSDNotice(0)

print "picmode"

a.setPictureMode('USER')
a.setPictureMode('asd')
a.setPictureMode(0)

print "mute"

a.setAudioMute('ON')
a.setAudioMute('asd')
a.setAudioMute(10)

print "delay"

a.setAudioDelay("OFF")
a.setAudioDelay('asdf')
a.setAudioDelay(0)

print "nr"
a.setNR('LOW')

print "ccol temp"
a.setColorTemp("WARM")

print "cont"
a.setContrast(5)

print "bright"
a.setBrightness(5)

print "hue"
a.setHue(5)

print "sat"
a.setSaturation(4)

print "sharp"
a.setSharpness(5)

print "pchp"
a.setPCHPosition(6)

print "pcvp"
a.setPCVPosition(6)

print "pcclock"
a.setPCClock(6)

print "pcphase"
a.setPCPhase(6)

print "red"
a.setRed(1)

print "green"
a.setGreen(1)

print "blue"
a.setBlue(9)

print "osdhpos"
a.setOSDHPosition(23)

print "osdvpos"
a.setOSDVPosition(12)

print "osdtime"
a.setOSDTimeout(6)

print "osdback"
a.setOSDTimeout(70)

print "reset"
a.setReset()
