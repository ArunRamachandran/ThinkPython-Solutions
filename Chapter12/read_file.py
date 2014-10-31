def read_file():
	fin = open('words.txt')
	# where , fin is the file object
	# File object provides several methods for reading, including 
	# readline etc.
	print fin
	line = fin.readline()
	print line
	

read_file()
