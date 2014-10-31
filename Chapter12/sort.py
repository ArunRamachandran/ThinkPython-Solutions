def sort_by_length(words):
	t = []
	for word in words:
		t.append((len (word), word))
	print t

	t.sort(reverse = True)

	print t

	import random

	res = []
	for length, word in t:
		print word
		res.append(word)
	print res

words = ['hello', 'uno', 'eby', 'xyz', 'world']

sort_by_length(words)
