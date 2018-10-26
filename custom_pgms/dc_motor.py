import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(40, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)

p = GPIO.PWM(40, 50)

p.start(7.5)

try:
    while True:
        GPIO.output(38, True)
        p.ChangeDutyCycle(5)
        time.sleep(2)
        GPIO.output(38, False)
        p.ChangeDutyCycle(7.5)
        time.sleep(2)
        p.ChangeDutyCycle(10)
        time.sleep(2)
        p.ChangeDutyCycle(12.5)
        time.sleep(2)
        p.ChangeDutyCycle(10)
        time.sleep(2)
        p.ChangeDutyCycle(7.5)
        time.sleep(2)
        p.ChangeDutyCycle(5)
        time.sleep(2)
        p.ChangeDutyCycle(2.5)
        time.sleep(2)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
