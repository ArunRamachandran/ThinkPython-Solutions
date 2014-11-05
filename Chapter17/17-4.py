class Point(object):
	''' class point to represent a point in 2 dimensional plane '''
	def __init__(self,x = 0,y = 0):
		self.x = x
		self.y = y
	
	def __str__(self):
		return '(%d %d)' % (self.x,self.y)

	def __add__(self,other):
		x = self.x + other.x
		y = self.y + other.y
		p = Point(x,y)
		return p

p1 = Point(3,4)
p2 = Point(6,5)

print "Points are "
print p1
print p2

print p1 + p2
