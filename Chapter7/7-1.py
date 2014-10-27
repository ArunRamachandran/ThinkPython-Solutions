# to write a fn print_n using Iteration instead of recursion

def print_n(s,n):
	print "\n"
	while n > 0:
		print s
		n = n - 1
	
n = input("Enter a no. :\n");
s = raw_input("enter a string :\n")

print_n(s,n)
