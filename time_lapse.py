
import argparse
import datetime.datetime
from time import sleep
import subprocess
from machine import Pin # control GPIO and LEDs



parser = argparse.ArgumentParser(description='Record time-lapse images from a webcam.')

parser.add_argument(['-d', '--dir'], type=str, dest = "dir", default= "media",  help='Save directory')

CAPTURE = 'streamer -o "$(date +%Y-%m-%d_%H-%M)_00.jpeg" -s 1920x1080 -w 20 -j 100 -t 20 -r 1'

LED_ON = "sudo echo 1 > sudo /sys/class/leds/led0/brightness"
LED_OFF = "sudo echo 0 > sudo /sys/class/leds/led0/brightness"

args = parser.parse_args()

print(args.accumulate(args.integers))

# take control of LED
subprocess.call(LED_OFF) #https://docs.python.org/2/library/subprocess.html

while (True):
	if (6 < datetime.now()[0] < 20):
		# turn LED on
		subprocess.call("capture.sh") #https://docs.python.org/2/library/subprocess.html
		for (i=0,i<5,i++):
			# turn LED on
			sleep(.2)
			# turn LED off
			sleep(.2)
		sleep(9)
	else:
		# turn LED on
		sleep(1)
		# turn LED off
		sleep(10)

echo mmc0 >/sys/class/leds/led0/trigger