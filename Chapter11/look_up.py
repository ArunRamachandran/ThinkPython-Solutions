def reverse_lookup(d,v):
	for keys in d:
		if d[keys] == v:
			print keys
	# raise ValueError

d = {"one" : "uno", "two" : "bqr", "three" : "hex", "four" : "hex"}
v = "hex"

reverse_lookup(d,v)
