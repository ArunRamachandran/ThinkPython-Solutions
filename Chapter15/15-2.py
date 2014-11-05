# write a fn names move_rectangle that takes a rectangle and two numbers 
# named dx and dy. It should change the location of the rectangle by adding
# dx to the x cordinate of corner and adding dy to the y coordinate of 
# corner

class rectangle(object):
	''' To represent a rectangle'''
class point(object):
	''' to represent a
		two dimensional point '''

def move_rectangle(rect,dx,dy):
	rect.corner.x += dx
	rect.corner.y += dy

	print "Moved Rectangle positions are "
	
	return rect

rect = rectangle()
rect.width = 100.0
rect.height= 200.0
rect.corner= point()
rect.corner.x = 0.0
rect.corner.y = 0.0

print "Initial position of rectangle "
print rect.corner.x
print rect.corner.y

rect = move_rectangle(rect,5,6)

print rect.corner.x
print rect.corner.y


