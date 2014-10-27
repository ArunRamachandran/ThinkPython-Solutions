# fn is_between(x,y,z) that returns a True if x<= y <= z or False

def is_between(x,y,z):
	if (y >= x) and (y <= z):
		return True
	else:
		return False

x = raw_input("Give x:\n")
y = raw_input("Give y:\n")
z = raw_input("Give z:\n")

case = is_between(x,y,z)

if case == True:
	print True
else:
	print True

