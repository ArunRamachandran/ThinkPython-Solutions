#The ackermann fn, A(m,n), is defined :
#	 {	n+1	if m== 0
#A(m,n) ={	A(m-1,1)if m > 0 and n ==0
#	 {	A(m-1,A(m,n-1)) if m > 0 and n > 0

# write a fn named ack thta evaluates Ackermann's fn.

def ack(m,n):
	if m == 0:
		return (n + 1)
	elif (m > 0 and n == 0):
		  return ack(m - 1,1)
	elif (m > 0 and n > 0):
		  return ack(m-1,ack(m,n-1))
	else:
		pass

m = input("Value for m:\n")
n = input("Value for n:\n")

print ack(m,n)
