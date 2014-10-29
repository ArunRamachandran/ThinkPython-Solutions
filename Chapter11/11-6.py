# Run the two versions of fibonacci witha range of parameters and compare
# their run times

known = {0 : 0, 1 : 1}

import time

def fib_with_dict(n):
	if n in known:
		return known[n]
	else :
		res = fib_with_dict(n-1) + fib_with_dict(n-2)
		known[n] = res
		return res

def fib_conv(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else :
		return (fib_conv(n-1) + fib_conv(n-2))

n = 30

print "Evaluating Conventional fib ,without dict !! "
print "n = ", + n
print "Starting Time :  ", 
start = time.time()
print start
x = fib_conv(n)
print "result ", + x
stop = time.time()
print "Stop time     :  ", 
print stop

print "Evaluating modified fib, using dict !! "
print "n = ", + n
print "starting time :  ",
start = time.time()
print start
res = fib_with_dict(n)
stop = time.time()
print "Result ", + res
print "stop Time     :  ",stop
