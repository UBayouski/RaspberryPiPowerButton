#!/usr/bin/python

import RPi.GPIO as GPIO
import subprocess

# Starting up
GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN)

# Wait until power button is off
# Recommended to use GPIO.BOTH for cases with switch
GPIO.wait_for_edge(3, GPIO.BOTH)

# Shutting down
subprocess.call(['shutdown', '-h', 'now'], shell=False)
