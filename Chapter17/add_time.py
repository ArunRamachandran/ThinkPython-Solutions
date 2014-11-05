class Time(object):
	''' class time to represent time of day '''
	def __init__(self,h = 0, m = 0, s = 0):
		self.h = h
		self.m = m
		self.s = s
	def __str__(self):
		return '%.2d:%.2d:%.2d' % (self.h,self.m,self.s)
	def __add__(self,other):
		if isinstance(other,Time):
			return self.add_time(other)
		else:	
			return self.increment(other)
	def add_time(self,other):
		self_seconds = self.time_to_int()
		other_seconds= other.time_to_int()
		tot = self_seconds + other_seconds
		return int_to_time(tot)
	def increment(self,other):
		seconds = self.time_to_int() + other
		return int_to_time(seconds)
	def time_to_int(time):
		seconds = time.h * 60 * 60 + time.m * 60 + time.s
		return seconds
	def __radd__(self,other):
		return self.__add__(other)

def int_to_time(seconds):
	t = Time()
	minutes,t.s = divmod(seconds,60)
	t.h,t.m = divmod(minutes,60)
	return t

time = Time(5,45,30)
print time

other= Time(4,25,50)
print other
'''
time = time.add_time(other)
print "Added time : ",
print time
'''
print time + other	
