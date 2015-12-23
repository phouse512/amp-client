# An abstraction built on top the python RPi.GPIO library, so that we can
# 	run, test, and build on a local environment


class GPIO(object):

	def __init__(self):
		raise NotImplementedError("you are attempting to call a method on an abstract class. Please use a concrete one")


	def set_pin(self):
		raise NotImplementedError("this is an abstract class")

# concrete class that handles when client/master is run on rasp pi
class RaspGPIO(GPIO):

	def __init__(self):
		try:
			import RPi.GPIO as GPIO

			GPIO.setmode(GPIO.BCM)

		except ImportError as e:
			print "Failed to import RPI, are you sure you are on the pi?"

# concrete class that handles when the client is run on a unix environment
class UnixGPIO(GPIO):

	def __init__(self):
		print "Unix GPIO, do nothing"