# My attempt to make another modified version of Q.No.11-4
# This code is valid if , values are unique

def invert_dict(d):
	inverse = dict()
	for keys in d:
		vals = d[keys]
		if vals not in inverse:
			inverse[vals] = keys		
	return inverse

d = {"one" : "uno", "two" : "hexa", "three" : "un", "four" : "hex"}
print "Dictionary"
print d
reverse = invert_dict(d)
print "Inverted Dictionary"
print reverse


