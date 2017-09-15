#!/usr/bin/python

import RPi.GPIO as GPIO
import subprocess

# Starting up
GPIO.setmode(GPIO.BCM)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(3, GPIO.IN)

# Light up the led button
GPIO.output(10, True)

# Wait until power button is off
GPIO.wait_for_edge(3, GPIO.RISING)

# Shutting down
subprocess.call(['shutdown', '-h', 'now'], shell=False)
