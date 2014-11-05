class Time(object):
	''' Class time to represent the time of day '''

def time_to_int(time):
	seconds = time.h * 60 * 60 + time.m * 60 + time.s
	return seconds

def int_to_time(seconds):
	clock = Time()
	minutes,clock.s = divmod(seconds,60)
	clock.h, clock.m = divmod(minutes,60)
	return clock

def increment(time,seconds):
	# attempt to write a pure fn
	import copy
	t = copy.copy(time)

	val = time_to_int(t)
	val = val + seconds
	t = int_to_time(val)
	print "Added time : ",
	print '%.2d:%.2d:%.2d' % (t.h,t.m,t.s)

time = Time()
time.h = 1
time.m = 0
time.s = 0

print "Time : ",
print '%.2d:%.2d:%.2d' % (time.h,time.m,time.s)
print "Time to add : 30 seconds"
increment(time,30)
