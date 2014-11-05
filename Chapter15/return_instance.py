class rectangle(object):
	''' class to represent a	
		rectangle '''

class point(object):
	''' to represent a 2 dimensional 
		point '''

def find_center(rect):
	p = point()
	p.x = rect.corner.x + rect.width/2.0
	p.y = rect.corner.y + rect.height/2.0
	
	return p

rect = rectangle()
rect.width = 100.0
rect.height= 200.0
rect.corner= point()
rect.corner.x = 0.0
rect.corner.y = 0.0

p = find_center(rect)
print '(%g %g)' % (p.x,p.y)
