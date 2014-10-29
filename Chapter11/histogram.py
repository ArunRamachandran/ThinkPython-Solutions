def histogram(s):
	d = dict()
	for c in s:
		if c not in d:
			d[c] = 1
		else :
			d[c] = d[c] + 1
	print d

s = "banana"
print s
histogram(s)

