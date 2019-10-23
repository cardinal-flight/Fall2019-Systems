import RPi.GPIO as GPIO
import time
import signal
import atexit

atexit.register(GPIO.cleanup)

pin = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT, initial=False)
p = GPIO.PWM(pin, 100)
p.start(0)
time.sleep(2)

p.ChangeDutyCycle(100)
time.sleep(2)

print("Finished")
