from functools import wraps
from client import ACTIVITY_PIN

def activity_led(amper_gpio):
	def decorator(f):
		@wraps(f)
		def decorated_function(*args, **kwargs):
			amper_gpio.output(ACTIVITY_PIN, amper_gpio.HIGH)
			rv = f(*args, **kwargs)
			amper_gpio.output(ACTIVITY_PIN, amper_gpio.LOW)
			return rv
		return decorated_function
	return decorator


def auth():
	def decorator(f):
		@wraps(f)
		def decorated_function(*args, **kwargs):
			rv = f(*args, **kwargs)
			return rv
		return decorated_function
	return decorator