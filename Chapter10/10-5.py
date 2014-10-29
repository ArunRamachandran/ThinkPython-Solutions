# To write a fn Chop, that takes the list , modifies it by removing
# the first and last elements, and returns None.

def chop(t):
	if len(t) > 0:
		del t[1:(len(t) - 1)]

t = ["a", "b", "c", "d"]
print "Befor Processing : ",
print t
print "After Processsing :",
chop(t)
print t

