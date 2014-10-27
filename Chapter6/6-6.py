# Code to check whether a given string is palondrome or not !!

def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]

def palindrome(word):
	l = len(word)
	if l != 0:
		f = first(word)
		lst = last(word)
		"""print f
		print lst"""
		if str(f) == str(lst):
			#print "In fn"
			word = middle(word)
			palindrome(word)
		else:
			return False
	if l == 0:
		return True

word = raw_input("Enter a word :\n")
case = palindrome(word)
if case == False:
	print "not a palindrome\n"
else:
	print "It's a palindrome\n"
