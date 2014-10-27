# In robert McCloskey's book "Make your Way for Ducklings", the names of the
# ducklings are Jack, Kack, Lack, Mack, Nack, ouack, Pack, and Quack.
# program "a.py" print that names in this order, except --Ouack and Quack--
# ( refer a.py)
# Modify the program to fix this error.

prefixes = "JKLMNOPQ"
suffix   = "ack"
special  = "uack"

for letter in prefixes:
	if letter == "O" or letter == "Q":
		print letter + special
	else :
		print letter + suffix

