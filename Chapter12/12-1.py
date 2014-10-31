# Write a fn called sumall that takes any no. of arguments and returns their
# their sum

def sumall(args):
	sum = 0
	for element in args:
		sum = sum + element
	print sum

tpl = (1,3,4)
print "Given Tuple : ", tpl
print "Sum :"
sumall(tpl)

