# Write a fn called remove_duplicates that takes a list and return a new
# list with only the unique elements from the original
#They dont have to be in the same order

def freq(char,orig):
	count = 0
	index = -1
	for letter in orig:
		index = index + 1
		if letter == char:
			count = count + 1
			store = index
	if count > 1:
		return store
	else :
		return False
		
			
def remove_duplicates(orig):
	copy = orig
	res  = []
	index= 0
	for char in orig:
		case
	
