from swampy.Gui import *
import Tkinter
import Image as PIL
import ImageTk

g = Gui()
g.title('Image Viewer')
canvas = g.ca(width = 400, height = 400)
photo = Tkinter.PhotoImage(file = 'danger.gif')
''' PhotoImage reads a file and returns a PhotoImage object that
Tkinter can display '''
canvas.image([0,0], image = photo)
g.la(image = photo)
g.bu(image = photo)
g.mainloop()
