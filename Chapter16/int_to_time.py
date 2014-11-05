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

time = int_to_time(60)
print "60 seconds : in time mode : ",
print '%.2d:%.2d:%.2d' % (time.hour,time.minute,time.seconds)

