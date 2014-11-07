from swampy.Gui import *

g = Gui()
g.title('19-2.py')

def make_create():
	item = canvas.circle([0,0], 100, fill = 'green')
def make_change():
	i = item.config(fill = 'red', outline = 'orange', width = 10)

canvas = g.ca(width = 500, height = 600)
b1 = g.bu(text = 'Press Button', command = make_create)
b2 = g.bu(text = 'Press To change', comman = make_change)

g.mainloop()
