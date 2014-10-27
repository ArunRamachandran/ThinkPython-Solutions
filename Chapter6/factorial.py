def factorial(n):
	if n == 0:
		return 1
	else:
		#rec = factorial(n - 1)
		#result = n * rec
		return (n * factorial(n-1))

x = input("enter a no. to find it's factorial\n")
y = factorial(x)
print y
