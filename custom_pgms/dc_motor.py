import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)

p = GPIO.PWM(12, 50)

p.start(7.5)

try:
    while True:
        p.ChangeDutyCycle(5)
        print '5'
        time.sleep(1)
        p.ChangeDutyCycle(7)
        print '7'
        time.sleep(1)
        p.ChangeDutyCycle(2)
        print '2'
        time.sleep(1)
        p.ChangeDutyCycle(10)
        print '10'
        time.sleep(1)
        p.ChangeDutyCycle(12)
        print '12'
        time.sleep(1)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
