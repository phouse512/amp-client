from flask import Flask
from gpio import GPIO, RaspGPIO, UnixGPIO

ALLOWED_PINS = [21, 26]
pi_client = None

def pi_initialization():
	# GPIO.setmode(GPIO.BCM)
	print "mocking the setup of GPIO pins"

	if "dev":
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



if __name__ == "__main__":
	pi_client = pi_initialization()
	app.run(host='0.0.0.0', port=5031)


