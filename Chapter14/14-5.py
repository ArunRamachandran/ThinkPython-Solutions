def linecount(filename):
	count = 0
	for line in open(filename):
		count += 1
	return count

print linecount('14-5.py')

