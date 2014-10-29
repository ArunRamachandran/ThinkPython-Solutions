# Write a fn. called has_duplicates , that takes a list and returns True
# if there is any element that appers more than once. 
# It should not modify the original list

def char_freq(char,string):
	count = 0
	for letter in string:
		if letter == char:
			count = count + 1
		else:
			pass
	return count
	
def has_duplicate(orig):
	count = 0
	index = 0
	for char in orig:
		count = char_freq(char,orig)
		if count > 1:
			return True
		else:
			pass

orig = raw_input("Give a string ?\n")
case = has_duplicate(orig)

if case == True:
	print "It has some duplicate characters !! "
else:
	print "Nope..!! It dont have repetative contents in it !! "


	
