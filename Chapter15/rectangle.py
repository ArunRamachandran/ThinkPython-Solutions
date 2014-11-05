# Creating a class object to represent a rectangle

class rectangle(object):
	''' Reepresents a rectangle
		'''

class point(object):
	''' to represent a 2 dimensional point'''

box = rectangle()
box.width = 100.0
box.height= 200.0
box.corner= point()
box.corner.x = 0.0
box.corner.y = 0.0

print "Class objects are... "
print "Width", box.width
print "Height", box.height
print "Corner points", box.corner.x, box.corner.y

