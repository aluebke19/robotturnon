import setup
from setup import RPL
import RoboPiLib as RPL
sensor_pin = 5
RPL.pinMode(sensor_pin,RPL.INPUT)
def analogRead(pin):
  putPacket(ANREAD, bytearray([5]), 1)
  buff = getPacket()
  return int(buff[3][1]) | (int(buff[3][2]) << 8)

while True:
  if RPL.analogRead(5) > 450 and RPL.analogRead(3) > 450:
    RPL.servoWrite(2,1490)
    RPL.servoWrite(1,300)
    print "ok"
  if 400 > RPL.analogRead(5) and RPL.analogRead(3) > 250:
    RPL.servoWrite(2,2000)
    RPL.servoWrite(1,1470)
    print "yeah"
  if RPL.analogRead(5) >= 400 and RPL.analogRead(5) <= 450:
    RPL.servoWrite(2,2000)
    RPL.servoWrite(1,300)
    print "gratata"
  if RPL.analogRead(3) < 250:
    RPL.servoWrite(2,2000)
    RPL.servoWrite(1,0)
  if RPL.digitalRead(17) == 0:
    break

while True:
  if RPL.digitalRead(17) == 0:
    RPL.servoWrite(2,2000)
    RPL.servoWrite(1,0)
  if RPL.digitalRead(17) == 1 and RPL.analogRead(3) > RPL.analogRead(5):
    break

while True:
  if RPL.analogRead(5) > 440 or RPL.analogRead(3) > 440:
    RPL.servoWrite(2,1490)
    RPL.servoWrite(1,300)
    print "ok"
  if RPL.analogRead(5) < 415 or RPL.analogRead(3) < 415:
    RPL.servoWrite(2,2000)
    RPL.servoWrite(1,1470)
    print "yeah"
  if RPL.analogRead(5) >= 420 or RPL.analogRead(5) <= 430:
    RPL.servoWrite(2,2000)
    RPL.servoWrite(1,300)
    print "gratata"
  if RPL.digitalRead(17) == 0:
    break

while True:
  if RPL.digitalRead(17) == 0:
    RPL.servoWrite(2,0)
    RPL.servoWrite(1,300)
  if RPL.digitalRead(17) == 1 and RPL.analogRead(3) > 420:
    break

while True:
  if RPL.analogRead(5) > 440 or RPL.analogRead(3) > 440:
    RPL.servoWrite(2,1490)
    RPL.servoWrite(1,300)
    print "ok"
  if RPL.analogRead(5) < 415 or RPL.analogRead(3) < 415:
    RPL.servoWrite(2,2000)
    RPL.servoWrite(1,1470)
    print "yeah"
  if RPL.analogRead(5) >= 420 or RPL.analogRead(5) <= 430:
    RPL.servoWrite(2,2000)
    RPL.servoWrite(1,300)
    print "gratata"
  if RPL.digitalRead == 0:
    break

while True:
  if RPL.analogRead(5) > 440 or RPL.analogRead(3) > 440:
    RPL.servoWrite(2,1480)
    RPL.servoWrite(1,2000)
    print "ok"
  if RPL.analogRead(5) < 415 or RPL.analogRead(3) < 415:
    RPL.servoWrite(2,500)
    RPL.servoWrite(1,1520)
    print "yeah"
  if RPL.analogRead(5) >= 420 or RPL.analogRead(5) <= 430:
    RPL.servoWrite(2,500)
    RPL.servoWrite(1,2000)
    print "gratata"
  if RPL.analogRead(0) < 300:
    break

while True:
  if RPL.analogRead(0) < 300:
    RPL.servoWrite(2,0)
    RPL.servoWrite(1,2000)
  if RPL.analogRead(0) > 400:
    break

while True:
  if RPL.analogRead(5) > 440 or RPL.analogRead(3) > 440:
    RPL.servoWrite(2,1480)
    RPL.servoWrite(1,2000)
    print "ok"
  if RPL.analogRead(5) < 415 or RPL.analogRead(3) < 415:
    RPL.servoWrite(2,500)
    RPL.servoWrite(1,1520)
    print "yeah"
  if RPL.analogRead(5) >= 420 or RPL.analogRead(5) <= 430:
    RPL.servoWrite(2,500)
    RPL.servoWrite(1,2000)
    print "gratata"
  if RPL.analogRead(5) < 300 and RPL.analogRead(3) > 300:
    break

while True:
  if RPL.analogRead(5) < 300 and RPL.analogRead(3) > 300:
    RPL.servoWrite(2,500)
    RPL.servoWrite(1,0)
  if RPL.analogRead(5) > RPL.analogRead(3):
    break

while True:
  if RPL.analogRead(0) > 440:
    RPL.servoWrite(2,1480)
    RPL.servoWrite(1,2000)
    print "ok"
  if RPL.analogRead(0) < 415:
    RPL.servoWrite(2,500)
    RPL.servoWrite(1,1520)
    print "yeah"
  if RPL.analogRead(0) >= 420:
    RPL.servoWrite(2,500)
    RPL.servoWrite(1,2000)
    print "gratata"
