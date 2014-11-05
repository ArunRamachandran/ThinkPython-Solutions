class Time(object):
	def print_time(self):
		''' by convention, the first parameter of a method is
	is called self '''
		print '%.2d:%.2d:%.2d' % (self.h,self.m,self.s)

time = Time()
time.h = 3
time.m = 49
time.s = 30
Time.print_time(time)
time.print_time()
