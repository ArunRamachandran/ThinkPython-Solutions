# Write a afn 'has_duplicates()', that takes a  list as a parameter and 
# returns True if there is any object that appears more than once in the list

def create_dict(lst):
	known = dict()
	for element in lst:
		if element not in known:
			known[element] = 1
		else:
			known[element] = known[element] + 1
	return known

def has_duplicates(lst):
	result = create_dict(lst)
	for element in result:
		if result[element] > 1:
			return True
	
lst = ["one", "two", "three", "two", "two"]
result = has_duplicates(lst)

print "Given List"
print lst
case = has_duplicates(lst)
if case == True:
	print "Yeah..!! It has some dupliate elements !!!"
else :
	print "Nope..!! It doesn't have duplicate elements !! "

