from functools import wraps


def activity_led(amper_gpio, activity_pin):
	def decorator(f):
		@wraps(f)
		def decorated_function(*args, **kwargs):
			amper_gpio.set_output_pin(activity_pin, amper_gpio.HIGH)
			rv = f(*args, **kwargs)
			amper_gpio.set_output_pin(activity_pin, amper_gpio.LOW)
			return rv
		return decorated_function
	return decorator


# def activity_led(amper_gpio, activity_pin):
# 	@wraps(f)
# 	def decorated_function(*args, **kwargs):
# 		amper_gpio.set_output_pin(activity_pin, amper_gpio.HIGH)
# 		rv = fn(*args, **kwargs)
# 		amper_gpio.set_output_pin(activity_pin, amper_gpio.LOW)
# 		return rv
# 	return decorated_function


def auth():
	def decorator(f):
		@wraps(f)
		def decorated_function(*args, **kwargs):
			rv = f(*args, **kwargs)
			return rv
		return decorated_function
	return decorator