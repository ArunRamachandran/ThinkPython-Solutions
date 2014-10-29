def reverse_lookup(d,v):
	res = []
	for keys in d:	
		if d[keys] == v:
			res.append(keys)
	return res

d = {"one" : "uno" , "two" : "hex", "three" : "hex"}
v = "hex"

result = reverse_lookup(d,v)

print "Given Dictionary : ",
print d
print "Value to Map : ",
print v
print "Keys corresponding to the given Value "
print result

