class Point(object):
	''' class point to represent a 2 dimensional point '''
	def __init__(self,x = 0, y = 0):
		self.x = x
		self.y = y

	def __str__(self):
		return '(%d %d)' % (self.x,self.y)

p = Point(3,4)

print p
