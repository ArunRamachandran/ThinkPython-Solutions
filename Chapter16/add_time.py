class Time(object):
	''' to represent the time of a day '''
t1 = Time()
t2 = Time()

t1.h = 4
t1.m = 61
t1.s = 0

t2.h = 1
t2.m = 59
t2.s = 0

def add_time(t1,t2):
	sum_time = Time()
	sum_time.h = t1.h + t2.h
	sum_time.m = t1.m + t2.m
	sum_time.s = t1.s + t2.s

	print "Without correction in sum -- "
	print "Sum of given times ",
	print '%.2d:%.2d:%.2d' % (sum_time.h, sum_time.m, sum_time.s)
	
	print "After modifying --"
	
	if sum_time.s > 60:	
		sum_time.s -= 60
		sum_time.m += 1

	if sum_time.m > 60:
		sum_time.m -= 60
		sum_time.h += 1

	print '%.2d:%.2d:%.2d' % (sum_time.h,sum_time.m,sum_time.s)


print "t1 ",
print '%.2d:%.2d:%.2d' % (t1.h, t1.m, t1.s)
print "t2 ",
print '%.2d:%.2d:%.2d' % (t2.h, t2.m, t2.s)

add_time(t1,t2)
