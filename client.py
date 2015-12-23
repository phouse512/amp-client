from flask import Flask
from gpio import InvalidRaspberryPiEnvironment
from gpio import RaspGPIO
from gpio import UnixGPIO

from sys import argv

ALLOWED_PINS = [21, 26]
pi_client = None

def pi_initialization(environment):
	print "mocking the setup of GPIO pins"
	if environment == 'dev':
		return UnixGPIO()
	else:
		return RaspGPIO()


# initialize the world here:
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"


@app.route("/status")
def status():
	print pi_client
	return "status"

@app.route("/toggle/<int:pin_out>")
def toggle_pin(pin_out):
	if pin_out not in ALLOWED_PINS:
		return 'invalid pin specified'

	pi_client.setup(pin_out, pi_client.OUTPUT)

	return "done"

if __name__ == "__main__":
	try:
		script, environment = argv
		pi_client = pi_initialization(environment)
		app.run(host='0.0.0.0', port=5031)
	except KeyboardInterrupt as e:
		print "fielded keyboard interrupt. Closing now."
	except InvalidRaspberryPiEnvironment as e:
		print e
		print "closing client server now"
	finally:
		if pi_client:
			pi_client.cleanup()


# TODO: add methods to handle GPIO cleanup