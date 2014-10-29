def invert_dict(d):
	inverse = dict()
	for keys in d:
		val = d[keys]
		if val not in inverse:
			inverse[val] = [keys]
		else:
			inverse[val].append(keys)
	return inverse

d = {"one" : "uno", "two" : "hexa", "three" : "uno", "four" : "hexa"}
print "Dictionary"
print d
reverse = invert_dict(d)
print "Inverted Dictionary"
print reverse


