def middle(t):	
	l = len(t)
	res = []
	if l > 0 and l % 2 == 0:
		l = l / 2
		res.append(t[l])
		res.append(t[l+1])
		return res
	if l > 0 and l % 2 != 0:
		l = l / 2
		res.append(t[l + 1])
		return res

t = ["a", "b", "c", "d","e"]
result = middle(t)

print "Initial List : ",
print t
print "Fn.Midlle Output : ",
print result
		
