# Write a fn called print_time that takes a Time object and prints it in the
# form  hour:minute:second.

class Time(object):
	''' To represent the 
	time of day '''

time = Time()
time.hour = 11
time.minutes = 9
time.second = 30

def print_time(time):
	print '%.2d:%.2d:%.2d' % (time.hour,time.minutes,time.second)

''' the format sequence '%.2d' prints an integer using atleast two digits,
including a leading zero if necessary. '''

print_time(time)
