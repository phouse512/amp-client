from flask import Flask
from gpio import InvalidRaspberryPiEnvironment

app = Flask(__name__)


def main():
	print "running"


@app.route("/scan")
def scan():
	print "scanning"


if __name__ == "__main__":
	try:
		main()
		app.run(host='0.0.0.0', port=5032)
	except KeyboardInterrupt as e:
		print "fielded keyboard. Closing now."
	except InvalidRaspberryPiEnvironment as e:
		print e
		print "closing client server now"
