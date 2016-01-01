import yaml
from sys import argv

from flask import Flask
from flask import jsonify
from commons import activity_led
from gpio import InvalidRaspberryPiEnvironment
from gpio import RaspGPIO
from gpio import UnixGPIO
from status import SET_STATUS_FAILURE
from status import SET_STATUS_SUCCESS


OUTLET_STATE_PIN = None
ACTIVITY_PIN = None
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
	return jsonify(client_id=server_conf['server_id'])


@app.route("/toggle/on")
@activity_led(pi_client, ACTIVITY_PIN)
def on():
	# turn on output status pin
	response = {}
	try:
		pi_client.set_output_pin(OUTLET_STATE_PIN, pi_client.LOW)
		response['status'] = SET_STATUS_SUCCESS
		response['data'] = pi_client.LOW
	except Exception as e:
		response['status'] = SET_STATUS_FAILURE
	return jsonify(response)


@app.route("/toggle/off")
@activity_led(pi_client, ACTIVITY_PIN)
def off():
	# turn on output status pin
	response = {}
	try:
		pi_client.set_output_pin(OUTLET_STATE_PIN, pi_client.HIGH)
		response['status'] = SET_STATUS_SUCCESS
		response['data'] = pi_client.HIGH
	except Exception as e:
		response['status'] = SET_STATUS_FAILURE
	return jsonify(response)

if __name__ == "__main__":
	try:
		script, environment = argv
		# initialize pi client
		pi_client = pi_initialization(environment)

		with open("conf/pin_conf.yml", 'r') as stream:
			pin_conf = yaml.load(stream)
			ACTIVITY_PIN = int(pin_conf['activity_pin'])
			OUTLET_STATE_PIN = int(pin_conf['output_pin'])

		# initialize pins for output on pi
		pi_client.setup(OUTLET_STATE_PIN, pi_client.OUTPUT)
		pi_client.setup(ACTIVITY_PIN, pi_client.OUTPUT)

		# load from file server id, if not there, create one <- not done yet
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