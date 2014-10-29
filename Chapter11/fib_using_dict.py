# Attempt to implement Fibonacci using a memos.
# Keeping track of values that have already ben computed by storing them
# in a dictionary.
# "A previously computed value that is stored for later use is called a memo

known = {0 : 0, 1 : 1}

def fib(n):
	if n in known:
		return known[n]
	res = fib(n-1) + fib(n-2)
	known[n] = res
	return res

print "fibonacci of ", + 4 
result = fib(4)
print result
print known

