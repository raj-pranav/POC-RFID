

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


def trigger_buz(intensity, duration):
    print ("Trigger started ..")
    GPIO.setup(buzzerPin, GPIO.OUT)
    pi_pwm = GPIO.PWM(buzzerPin, 500)  # pin with frequency

    pi_pwm.start(0) # Start with this duty cycle

    # set a pwm between 0 - 100
    pi_pwm.ChangeDutyCycle(intensity)
    time.sleep(duration)
    pi_pwm.stop()
    GPIO.cleanup()
    print ("Trigger ENDs")

if __name__ == "__main__":
    print ("Executing directly from the same module")
    trigger_buz(0, 0)


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
