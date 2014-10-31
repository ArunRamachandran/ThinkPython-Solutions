# has_match takes two sequences, t1 and t2, and returns True, if there is
# an index i such that t1[i] == t2[i]

def has_match(t1,t2):
	for x,y in zip(t1,t2):
		if x == y:
			return True
		else:
			return False

t1 = "banana"
t2 = "sequence"

print "Given sequences are : "
print t1
print t2

case = has_match(t1,t2)
if case == True:
	print "Yeah..!! Two sequences have a matching index "
if case == False:
	print "Nope... It doesn't have a matching index !! "


