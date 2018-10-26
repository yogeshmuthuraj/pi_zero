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
        time.sleep(2)
        p.ChangeDutyCycle(7.5)
        print '7.5'
        time.sleep(2)
        p.ChangeDutyCycle(10)
        print '10'
        time.sleep(2)
        p.ChangeDutyCycle(12.5)
        print '12.5'
        time.sleep(2)
        p.ChangeDutyCycle(10)
        print '10'
        time.sleep(2)
        p.ChangeDutyCycle(7.5)
        print '7.5'
        time.sleep(2)
        p.ChangeDutyCycle(5)
        print '5'
        time.sleep(2)
        p.ChangeDutyCycle(2.5)
        print '2.5'
        time.sleep(2)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
