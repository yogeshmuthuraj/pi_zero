import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 50)

p.start(7.5)

try:
    while True:
        p.ChangeDutyCycle(7.5)  # turn towards 90 degree
        p.stop()
        time.sleep(5) # sleep 1 second
        p.ChangeDutyCycle(2.5)  # turn towards 0 degree
        p.stop()
        time.sleep(5) # sleep 1 second
        p.ChangeDutyCycle(12.5) # turn towards 180 degree
        p.stop()
        time.sleep(5) # sleep 1 second
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
