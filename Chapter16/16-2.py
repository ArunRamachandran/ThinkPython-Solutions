class Time(object):
	''' To represent the
 time of day '''

t1 = Time()
t2 = Time()

t1.h = 4
t1.m = 59
t1.s = 30

t2.h = 2
t2.m = 30
t2.s = 15

def print_time(t1,t2):
	print "t1 :",
	print '%.2d:%.2d:%.2d' % (t1.h,t1.m,t1.s)
	print "t2 :",
	print '%.2d:%.2d:%.2d' % (t2.h,t2.m,t2.s)

def is_after(t1,t2):
	t1_sec = t1.h*60*60 + t1.m*60 + t1.s
	t2_sec = t2.h*60*60 + t2.m*60 + t2.s

	return t1_sec > t2_sec
	''' conditional operation will return either True or False
according to the evaluation of the statements '''

print_time(t1,t2)
case = is_after(t1,t2)

print case
