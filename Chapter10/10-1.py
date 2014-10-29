def capitalize_all(t):
	res = []
	for element in t:
		res.append(element.capitalize())
	return res

t = ["a","b", ["x", "y"]]
print t
result = capitalize_all(t)

