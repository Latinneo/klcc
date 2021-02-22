#!/usr/bin/env python3

import leglight

myLight = leglight.LegLight('192.168.0.29',9123)
if myLight.isOn == 0:
    myLight.on()
    myLight.brightness(15)
    myLight.color(4300)
else:
    myLight.off()
