import math

def distance_bw_points(x,y):
	distance = math.sqrt(x**2+y**2)
	print distance

class points():
	''' class to create a 2 dimension point'''

blank = points()
blank.x = 3.0
blank.y = 4.0
print "Given points are..",
print '%g %g' % (blank.x, blank.y)
print "Calling Fn."
distance_bw_points(blank.x,blank.y)

