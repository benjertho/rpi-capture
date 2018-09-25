

import datetime.datetime
from time import sleep
import subprocess

# take control of LED
subprocess.call() #https://docs.python.org/2/library/subprocess.html

while (True):
	if (6 < datetime.now()[0] < 20):
		# turn LED on
		subprocess.call() #https://docs.python.org/2/library/subprocess.html
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
