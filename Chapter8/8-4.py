def find(word,letter,pos):
	index = pos
	while index < len(word):
		if word[index] == letter:
			return index
		index = index + 1
	return -1

word = raw_input("Give a word :\n")
letter = raw_input("Enter a leter\n")
pos = input("Give a positon tosearch frpm\n")

x = find(word,letter,pos)
print x
