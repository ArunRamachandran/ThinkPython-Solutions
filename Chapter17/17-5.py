class Point(object):
	''' class point is to represent a 2 dimensioanl point '''
	def __init__(self,x = 0,y = 0):
		self.x = x
		self.y = y

	def __str__(self):
		return '(%d %d)' % (self.x,self.y)

	def __add__(self,other):
		if isinstance(other,Point):
			return self.add_points(other)
		else :
			return self.add_tuples(other)

	def add_points(self,other):
		p = Point()
		p.x = self.x + other.x
		p.y = self.y + other.y
		return p
	def add_tuples(self,other):
		p = Point()
		p.x = self.x + int(other[0])
		p.y = self.y + int(other[1])
		return p

p1 = Point(3,6)
print p1

p2 = Point(4,5)
print p2

print p1 + p2
