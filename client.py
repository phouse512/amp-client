from flask import Flask
#import RPi.GPIO as GPIO

ALLOWED_PINS = [21, 26]

def pi_initialization():
	# GPIO.setmode(GPIO.BCM)
	print "mocking the setup of GPIO pins"

# initialize the world here:
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"


@app.route("/status")
def status():
	return "status"

@app.route("/toggle/<int:pin_out>")
def toggle_pin(pin_out):
	if pin_out not in ALLOWED_PINS:
		return 'invalid pin specified'


	# GPIO.output(pin_out)


if __name__ == "__main__":
	pi_initialization()
	app.run(host='0.0.0.0', port=5031)


