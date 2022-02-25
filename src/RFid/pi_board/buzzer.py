

"""
-----------------------------------------------
IMPLEMENTATION using RPi.GPIO   --|
-----------------------------------------------

"""

import RPi.GPIO as GPIO
import time

buzzerPin = 32  # GPIO pin: 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(buzzerPin, GPIO.OUT)
pi_pwm = GPIO.PWM(buzzerPin, 500)  # pin with frequency

def trigger_buz(intensity, duration):
    pi_pwm.start(0) # Start with this duty cycle

    # set a pwm between 0 - 100
    pi_pwm.ChangeDutyCycle(intensity)
    time.sleep(duration)
    pi_pwm.stop()
    GPIO.cleanup()

if __name__ == "__main__":
    trigger_buz(1, 1)


"""
-----------------------------------------------
IMPLEMENTATION using GPIOZero - NOt working !!
-----------------------------------------------

import gpiozero as gpz
import time

buzzerPin = 12 # BCM pin ref

bz = gpz.Buzzer(buzzerPin, active_high=False, initial_value=False)
bz.on()
bz.beep(on_time = 0.5, off_time = 1, n = 4)

"""
