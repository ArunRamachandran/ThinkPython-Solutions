from swampy.Gui import *

g = Gui()
g.la('Select a color:')
colors = ['red', 'green', 'blue']
mb = g.mb(text = colors[0])

def set_color(color):
	mb.config(text = color)
	print color

for color in colors:
	g.mi(mb, text = color, command = Callable(set_color, color))

g.mainloop()
