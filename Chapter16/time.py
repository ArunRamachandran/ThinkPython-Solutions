# Code that convert given integer ( i.e seconds) to Time

class Time(object):
	''' class to represent the time of day '''

def int_to_time(seconds):
	time = Time()
	minutes, time.seconds = divmod(seconds,60)
	time.hour, time.minute= divmod(minutes,60)
	return time

''' where , divmod() divides the first argument by the second and returns
the quotient and remainder as a tuple '''

def time_to_int(time):
	seconds = time.hour * 60 * 60 + time.minute * 60 + time.seconds
	return seconds


