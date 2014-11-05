# Attempt to write a pure fn

class Time(object):	
	''' to represent a time of day '''

time = Time()
time.h = 5
time.m = 35
time.s = 40

def increment(time,seconds):
	import copy
	t = copy.copy(time)
	
	t.s += seconds

	if t.s >= 60:
		val = t.s / 60
		t.s -= (60 * val)
		t.s += val
	if t.m >= 60:
		val = t.m / 60
		t.m -= (60 * val)
		t.m += val

	return t

print "Time : ",
print '%.2d:%.2d:%.2d' % (time.h,time.m,time.s)
new_time = increment(time,15)
print "Modified Time :",
print '%.2d:%.2d:%.2d' % (new_time.h,new_time.m,new_time.s)

increment(time,10)
