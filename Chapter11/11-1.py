# Write a fn that reads the words in words.txt and stores them as keys in a
# dictionary. It doesn't matter what the values are.

def read_file():
	word = open('words.txt').read().split()
	length = len(word)
	dct = dict()
	i   = 0
	for char in word:
		dct[char] = i
		i = i + 1
	print dct	

read_file()




