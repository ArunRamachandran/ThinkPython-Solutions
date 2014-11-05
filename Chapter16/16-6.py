class Time(object):
	''' class time is used to represent the time of day '''

def time_to_int(time):
	seconds = time.h * 60 * 60 + time.m * 60 + time.s 
	return seconds

def int_to_time(seconds):
	clock = Time()
	minutes,clock.s = divmod(seconds,60)
	clock.h,clock.m = divmod(minutes,60)
	return clock

def mul_time(time,number):
	import copy
	new_time= copy.copy(time)
	seconds = time_to_int(time)
	product = seconds * number
	new_time= int_to_time(product)
	print "Multiplied time : ",
	return new_time

time = Time()
time.h = 2
time.m = 0
time.s = 0

print "Present Time : ",
print '%.2d:%.2d:%.2d' % (time.h,time.m,time.s)

number = 4
print "Value to get multiplied : %d" % (number)

new_time = mul_time(time,number)
print "Multiplied time : ",
print '%.2d:%.2d:%.2d' % (new_time.h,new_time.m,new_time.s)

