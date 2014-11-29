#!/usr/bin/python

import datetime,time
from Adafruit_I2C import Adafruit_I2C

def showChar(c):
  bytes=[]
  for item in c:
    bytes.append( ((item & 0xFE)>>1)|((item & 0x01)<<7) )
    bytes.append(0x00)
    i2c.writeList(0x00,bytes)

print "Pi World Clock"
i2c=Adafruit_I2C(address=0x70)
i2c.write8(0x21,0x00)
i2c.write8(0x81,0x00)
i2c.write8(0xe0 | 0x01,0x00)
smile=[0x3C,0x42,0x95,0xA1,0xA1,0x95,0x42,0x3c]
showChar(smile)
