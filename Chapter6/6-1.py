# Write a compare fn. that returns 1 if x > y, 0 if x == y, and -1 if x < y

def compare(x,y):
	if (x > y):
		return 1
	elif x == y:
		return 0
	elif x < y:
		return -1
	else:
		pass

x = raw_input("Enter x:\n")
y = raw_input("Enter y:\n")

z = compare(x,y)
print z
