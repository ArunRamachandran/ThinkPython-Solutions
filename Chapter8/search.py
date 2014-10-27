def find(word,letter):
	index = 0
	while index < len(word):
		if word[index] == letter:
			return index
		index = index + 1
		
	return -1

word = raw_input("Give a string?\n")
letter = raw_input("Give a letter to search!\n")

x = find(word,letter)

print x
