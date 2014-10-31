# Write a fn called most_frequent that takes a string and prints the letters
# in decreasing order of frequency.

def count_char(string,char):
	count = 0
	for word in string:
		if word == char:
			count = count + 1
	return count 
	
def most_frequent(string):
	res = []
	for char in string:
		count = count_char(string,char)
		res.append((count,char))
	
	res.sort(reverse = True) # To sort in decreasing order
	
	t = []
	
	for count,char in res:
		if char not in t:
			t.append(char)
		else:
			pass
	
	print t


string = "ThinkPython"
most_frequent(string)
