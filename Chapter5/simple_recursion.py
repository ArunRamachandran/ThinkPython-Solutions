# attempt to implement a simple recursion fn 

def count_down(n):
	if n <= 0:
		print "Blastoff !"
	else:
		print n
		count_down(n-1)

count_down(5)
