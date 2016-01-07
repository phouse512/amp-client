# An abstraction built on top the python RPi.GPIO library, so that we can
# 	run, test, and build on a local environment

from commons import InvalidRaspberryPiEnvironment

try:
	import RPi.GPIO as GPIO

except ImportError as e:
	print "Failed to import RPI, are you sure you are on the pi?"

# abstract class
class AmpGPIO(object):

	INPUT = 1
	OUTPUT = 0

	HIGH = 1
	LOW = 0

	def __init__(self):
		raise NotImplementedError("you are attempting to call a method on an abstract class. Please use a concrete one")


	def set_output_pin(self, pin, level):
		raise NotImplementedError("this is an abstract class")


	def setup(self, pin, type):
		raise NotImplementedError("this is an abstract class")

	def cleanup(self):
		raise NotImplementedError("this is an abstract class")

# concrete class that handles when client/master is run on rasp pi
class RaspGPIO(AmpGPIO):

	def __init__(self):
		print "ma"
		# try:
		# 	import RPi.GPIO as GPIO
		#
		# 	GPIO.setmode(GPIO.BCM)
		#
		# 	# this bad.. don't forget to abstract pin specific calls out of this class
		# 	GPIO.setup(21, GPIO.OUT)
		# 	GPIO.output(21, GPIO.LOW)
		#
		# except ImportError as e:
		# 	print "Failed to import RPI, are you sure you are on the pi?"
		# 	raise InvalidRaspberryPiEnvironment("invalid raspberry pi environment")

	def set_output_pin(self, pin, level):

		if level == self.HIGH:
			GPIO.output(pin, GPIO.HIGH)
		elif level == self.LOW:
			GPIO.output(pin, GPIO.LOW)
		else:
			print "failed to set output"


	def setup(self, pin, type):

		if type == self.INPUT:
			GPIO.setup(pin, GPIO.IN)
		elif type == self.OUTPUT:
			GPIO.setup(pin, GPIO.OUT)
		else:
			print "failed to setup pi: invalid type."

	def cleanup(self):
		GPIO.cleanup()

# concrete class that handles when the client is run on a unix environment
class UnixGPIO(AmpGPIO):

	def __init__(self):
		print "Unix GPIO, do nothing"


	def set_output_pin(self, pin, level):
		print "pin %s has been set to level: %s" % (str(pin), str(level))

	def setup(self, pin, type):
		print "pin %s has been set to type: %s" % (str(pin), str(type))

	def cleanup(self):
		print "mocking cleaning up."



