# Write a fn called do_n that takes a fn objct and a number, n, as
# arguments, and that calls the given fn n times.

def do_n(f,n):
	if n <= 0:
		return
	else:
		f()
		do_n(f,n-1)

def print_hello():
	print "Hello"

do_n(print_hello,5)
