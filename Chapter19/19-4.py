from swampy.Gui import *

import Image as PIL
import ImageTk

g = Gui()
g.title('Image Viewer')
photo = PhotoImage(file = 'danger.gif')
canvas.image([0,0], image = photo)
g.mainloop()
