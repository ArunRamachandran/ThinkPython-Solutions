from swampy.Gui import *

g = Gui()
g.title('19-3.py')
canvas = g.ca(width = 500, height = 600, bg = 'white')
circle = None

def make_circle():
	circle = canvas.circle([0,0], 100)
def make_change():
	if circle == None:
		return
	color = entry.get()
	try:
		circle.config(fill = color)
	except TclError, message:
		print message


b1 = g.bu(text = 'Create Circle', command = make_circle)
entry = g.en()
b2 = g.bu(text = 'Press to Config', command= make_change)

g.mainloop()
