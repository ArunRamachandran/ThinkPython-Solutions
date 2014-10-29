# Two words are anagrams if you can rearrange the letters from one to spell
# the other. Write a fn. called is_anagram that takes two strings and 
# returns True if they are anagrams

orig = raw_input("Enter a string\n")
check= raw_input("Enter a word, to check its presence in Previous\n")

def is_anagram(orig,check):
	count = 0
	for letter in check:
		for chara in orig:
			if letter == chara:
				count = count + 1
		if count == 0:
			return False
		else:
			count = 0

print "Original String : ",
print orig
print "String, to detect : "
print check

case = is_anagram(orig,check)
if case == False:
	print "They are Not Anangrams !"
else:
	print "Wow..!! Anagrams !! "
		
