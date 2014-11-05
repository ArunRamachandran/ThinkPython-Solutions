class Time(object):
	''' class to represent the time of day '''
	def time_to_int(self):
		seconds = self.h * 60 * 60 + self.m * 60 + self.s
		return seconds
	def is_after(self,other):
		return self.time_to_int() > other.time_to_int()

time = Time()
other= Time()

time.h = 4
time.m = 30
time.s = 15

other.h = 2
other.m = 30
other.s = 45

case = time.is_after(other)
print case

