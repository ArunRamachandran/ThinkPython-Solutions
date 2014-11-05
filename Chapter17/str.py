class Time(object):
	''' class time to represent the tie of day '''
	def __init__(self,h = 0,m = 0,s = 0):
		self.h = h
		self.m = m
		self.s = s

	def __str__(self):
		return '%.2d:%.2d:%.2d' % (self.h,self.m,self.s)

time = Time(9,30,45)
'''
time.h = 9
time.m = 30
time.s = 45 
'''
print time
