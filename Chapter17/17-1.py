class Time(object):
	''' class to represent the time of day '''
	def time_to_int(self):
		seconds = self.h * 60 * 60 + self.m * 60 + self.s
		return seconds

time = Time()
time.h = 3
time.m = 45
time.s = 10

print "Time : ",
print '%.2d:%.2d:%.2d' % (time.h,time.m,time.s)
seconds = time.time_to_int()
print "Given time in seconds : ",
print seconds
