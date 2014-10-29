def histogram(s):
	d = dict()
	for c in s:
		value = d.get(c,0)
		if value == 0:
			d[c] = 1
		else :
			d[c] = d[c] + 1
	print d

s = "banana"
print s
histogram(s)

