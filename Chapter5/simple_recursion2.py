# To write a fn, that prints a string n times

def print_n(s,n):
	if n <= 0:
		return 
	print s
	print_n(s,n-1)

s = raw_input("String ?\n")
print_n(s,5)
