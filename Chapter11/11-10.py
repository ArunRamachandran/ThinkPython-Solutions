# Two word are rotate pairs if we can rotate one of them and get other 
# Write a program that reads a wordlist and finds all the rotate pairs

def is_rotate_pair(element):
	reverse = element[::-1]
	if reverse == element:
		return True
	else :
		return False

def rotate(lst):
	d = dict()
	for element in lst:
		case = is_rotate_pair(element)
		if case == True:
			d[element] = "True"
		else:
			d[element] = "False"
	return d  # Returning created dictionary from fn

lst = ["word", "list", "heleh"]
result = rotate(lst)
print "Given List : "
print lst
print "Rotate pairs : "
for elements in result:
	if result[elements] == "True":
		print elements
