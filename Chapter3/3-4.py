# A fn. object is a value you can assign to a variable or pass as an argument
# 'do_twice' is a fn that take a fn objct as an argument and calls it twice
#
def print_spam():
	print "spam"

def do_twice(f):
	f()
	f()

do_twice(print_spam)

# 2.Modify do_twice so that it takes two arguments, a fn objct and a value,
# and calls the fn twice, passing the value as an argument.

word = raw_input("Enter a word..\n")

def print_spam(word):
	print word

def do_twice(f,word):
	f(word)
	f(word)

do_twice(print_spam,word)


#3. Write a grn. version of print_spam, called  print_twice, that takes a 
# a string as a paramtere and print it twice.

word = raw_input("Enter a string\n");

def print_twice(word):
	print word
	print word

print_twice(word)	

#4. Use the modified version of do_twice to call print_twice, passing 'spam'
# as an argument.

print "\n"

def do_twice(word):
	print_twice(word)
	print_twice(word)

def print_twice(word):
	print word

s = "hello"

do_twice(s)

# 5.Define a new fn. called do_four(), that takes a fn object and a value
# and calls the fn four times, passing the values as a parameter . There
# should be only two statements in the body of this fn, not four

obj = raw_input("Give a string .\n")

def f(obj):
	print obj

def do_twice(f,obj):
	f(obj)
	f(obj)

def do_four(f,obj):
	do_twice(f,obj)
	do_twice(f,obj)	

do_four(f,obj)
