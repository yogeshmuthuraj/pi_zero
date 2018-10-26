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
        time.sleep(0.5)
        p.ChangeDutyCycle(6)
        time.sleep(0.5)
        p.ChangeDutyCycle(7)
        time.sleep(0.5)
        p.ChangeDutyCycle(6)
        time.sleep(0.5)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
