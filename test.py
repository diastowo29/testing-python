from gpiozero import LED
from time import sleep

pinEnable = LED(13)
pinDir = LED(19)
pinPulse = LED(21)

pinEnable.on()
pinDir.on()

while True:
    pinPulse.on()
    sleep(1/1000)
    pinPulse.off()
    sleep(1/1000)