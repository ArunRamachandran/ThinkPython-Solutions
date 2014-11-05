class Time(object):
	''' class time to represent a time of day '''
	def __init__(self,h = 0, m = 0, s = 0):
		self.h = h
		self.m = m
		self.s = s

	def __str__(self):
		return '%.2d:%.2d:%.2d' % (self.h, self.m, self.s)

	def __cmp__(self, other):
		t1 = self.h, self.m, self.s
		t2 = other.h, other.m, other.s
		return cmp(t1,t2)


t1 = Time(4,36,50)
print t1
t2 = Time(9,15,20)
print t2

print cmp(t1,t2)
