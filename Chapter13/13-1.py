# To write a program that reads a file, breaks each line into words, strips
# white spaces and punctuation from the words and converts them to lowercase

def read_file(filename):
	res = []
	fin = open(filename)
	for line in fin:
		word = line.split()
		print word
#		word = w.strip().lower()
#		word = line.strip().lower()
#		print word

read_file('python.txt')

	
