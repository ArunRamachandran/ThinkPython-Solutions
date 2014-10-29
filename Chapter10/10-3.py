# Write a fn that takes a list of numbers and return a the Cumulative sum
# For eg: the cumulative sum of [1,2,3] is [1,3,6]

t = [1,2,3]

def cumulative_sum(t):
	sum = 0
	res = []
	for element in t:
		sum = sum + element
		res.append(sum)
	return res

x = cumulative_sum(t)

print "Cumulative Sum of ",
print t,
print "is  : ",
print x 
