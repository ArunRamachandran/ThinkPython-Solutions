class Point(object):
	''' class point to represent a point in 2 dimensional 
plane'''
	def __init__(self,x = 0, y = 0):
		self.x = x
		self.y = y
	def print_point(self):
		print '(%d %d)' % (self.x,self.y)

coordinate = Point()
coordinate.print_point()

p = Point(5,6)
p.print_point()
