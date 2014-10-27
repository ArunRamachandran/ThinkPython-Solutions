# more general version of factorial, which will only accept Int values

def factorial(n):
	if not isinstance(n,int):
		print "Factorial only work with Integetrs !"
	elif n < 0:
		print "Factorial is not define for Negative Numbers !"
	elif n == 0:
		return 1
	else :
		return (n * factorial(n-1))

x = input("Give a number:\n")
print factorial(x)
