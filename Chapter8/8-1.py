# To write a fn that takes a string as an argument and displays the letters backward,one per line

def reverse_str(string):
	l = len(string)
	while l > 0:
		print string[l - 1]
		l = l - 1;

string = raw_input("Enter a string : \n")
reverse_str(string)
