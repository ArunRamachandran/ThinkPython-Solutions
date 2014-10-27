# to find GCD 

def gcd(a,b):
	if b == 0:
		return a
	elif a == 0:
		return b
	else:
		r = a % b
		return gcd(b,r)

a = 9
b = 27

result = gcd(a,b)
print result
