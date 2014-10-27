def counting(word,char):
	count = 0
	for letter in word:
		if letter == char:
			count = count + 1
	print count

word = "banana"
print word
print "Counting no.of times 'a' appeears in string"
counting(word,"a")
