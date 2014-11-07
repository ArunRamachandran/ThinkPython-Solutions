import os

from swampy.Gui import *
import Tkinter
import Image as PIL
import ImageTk

g = Gui()
g.title('Image Viewer')
canvas = g.ca(width = 500, height = 500, bg = 'white')

def walk(dirname):
	for name in os.listdir(dirname):
		path = os.path.join(dirname, name)
		if os.path.isfile(path):
			try:
				show_image(name)
				print name
				g.mainloop()
			except:
				pass
		else:
			walk(path)

def show_image(fp):
	image = PIL.open(fp)
	tkpi  = ImageTk.PhotoImage(image)
	canvas(image = tkpi)

print 'Directory :'
cwd = os.getcwd()
print cwd

walk(cwd) 			

