# To add up all elements in a list

def add_all(t):
	total = 0
	for element in t:
		total = total + element
	return total

t = [10,20, 30, 40, 50]
print "List :  ",
print t
print "Sum of all elements in the list : "
sum = add_all(t)
print sum

