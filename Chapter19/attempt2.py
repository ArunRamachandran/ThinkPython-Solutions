from swampy.Gui import *

g = Gui()
g.title('Event')

def make_circle(event):
	pos = canvas.canvas_coords([event.x, event.y])
	item = canvas.circle(pos, 5, fill = 'red')

canvas = g.ca(width = 400, height = 400, bg = 'white')
canvas.bind('<ButtonPress-1>', make_circle)
g.mainloop()
