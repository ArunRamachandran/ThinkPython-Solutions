class Time(object):
	''' class time to represent time of day '''

def time_to_int(time):
	seconds = time.h * 60 * 60 + time.m * 60 + time.s
	return seconds

time = Time()
time.h = 1
time.m = 0
time.s = 0

print "Given time : ",
print "%.2d:%.2d:%.2d" % (time.h,time.m,time.s)
seconds = time_to_int(time)
print "Given time in int : ",
print seconds

