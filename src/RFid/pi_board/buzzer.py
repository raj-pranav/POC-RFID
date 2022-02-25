
import RPi.GPIO as GPIO
import time

buzzerPin = 32  # GPIO pin: 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(buzzerPin, GPIO.OUT)
pi_pwm = GPIO.PWM(buzzerPin, 1000)  # pin with frequency
pi_pwm.start(0)

# set a pwm between 0 - 100
duty_cyc = 10
pi_pwm.ChangeDutyCycle(duty_cyc)
time.sleep(2)
pi_pwm.ChangeDutyCycle(0)
