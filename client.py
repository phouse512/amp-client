import yaml

from flask import Flask
from decorators import activity_led
from gpio import InvalidRaspberryPiEnvironment
from gpio import RaspGPIO
from gpio import UnixGPIO

from sys import argv


OUTLET_STATE_PIN = 26
ACTIVITY_PIN = 21

pi_client = None

def pi_initialization(environment):
	print "mocking the setup of GPIO pins"
	if environment == 'dev':
		return UnixGPIO()
	else:
		return RaspGPIO()


# initialize the world here:
app = Flask(__name__)

@app.route("/status")
def status():
	return str(server_conf['server_id'])

@app.route("/toggle/<int:pin_out>")
def toggle_pin(pin_out):

	pi_client.setup(pin_out, pi_client.OUTPUT)

	return "done"

@app.route("/toggle/on")
@activity_led()
def on():
	# turn on output status pin
	return "done"

if __name__ == "__main__":
	try:
		script, environment = argv
		pi_client = pi_initialization(environment)

		# load from file server id, if not there, create one
		with open("conf/client_conf.yml", 'r') as stream:
			server_conf = yaml.load(stream)

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