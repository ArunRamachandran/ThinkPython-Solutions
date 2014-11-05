# Write a version of move_rectangle that creats and returns a new rectangle
# instead of modifying the old one.

import copy

class rectangle(object):
	''' to store a rectangle '''

class point(object):
	''' to represent a  2 dimensional
		point '''

def move_rectangle_v2(rect,dx,dy):
	new_rect = copy.copy(rect)
	new_rect.corner.x += dx
	new_rect.corner.y += dy

	return new_rect

rect = rectangle()
rect.height = 100.0
rect.width  = 200.0
rect.corner = point()
rect.corner.x = 0.0
rect.corner.y = 0.0

print "Initial rect. corner",
print '(%g %g)' % (rect.corner.x,rect.corner.y)

new_rect = move_rectangle_v2(rect,5,6)	
print "Passing arguments : dx,dy",
print '5 6'

print "Moved Rectanlge corner",
print '(%g %g)' % (new_rect.corner.x, new_rect.corner.y)

