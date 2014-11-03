'''def signature(s):
    """Returns the signature of this string, which is a string
    that contains all of the letters in order.
    """
    t = list(s)
    print t
    t.sort()
    print t
    t = ''.join(t)
    print t
'''
def is_anagram(word,lst):
	for element in lst:
		if element == word:
			pass
		else :
			length = len(element)
			if length < len(word):
				return False
			else :
				for char in word:
					if char not in element:
						return False

def anagrams(filename):
	d = []
	for line in open(filename):
		word = line.strip()
		d.append(word)
	print d
		
		
	
anagrams('text_12-4.txt')
#print s
