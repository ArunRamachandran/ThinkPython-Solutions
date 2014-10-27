
def boarder():
	print "+","-" * 5,"+","-" * 5, "+"

def side_lines():
	row = "|" + " " * 7+ "|" + " " * 7 + "|"
	print row 
	print row
	print row
	print row

def side_line_without_n():
	print "|" + " " * 6 + "|" + " " * 6 + "|"

def square():
	boarder()
	side_lines()
	boarder()
	side_lines()
	boarder()

square()


