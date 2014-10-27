# Write a fn.named 'right_justify' that takes a string named S as a
# parameter and prints the string wit enough leading spaces so that
# the letter of the string is in column 70 of the display
# >>>right_justify('allen')


word = raw_input('Word ? \n')

def right_justify(s):
	print " " * (70 - len(word)) + word

right_justify(word)
