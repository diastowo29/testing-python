from gpiozero import LED
from time import sleep

pinEnable = LED(13)
pinDir = LED(19)
pinPulse = LED(21)

pinEnable.off()
pinDir.on()

while True:
    pinPulse.on()
    print('hehe')
    sleep(1/1000)
    pinPulse.off()
    print('haha')
    sleep(1/1000)

pinEnable.on()
pinDir.off()