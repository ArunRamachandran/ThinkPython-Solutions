from swampy.Gui import *

g = Gui()
g.title('Gui')

def make_button():
	b2 = g.bu(text = 'Press here too..!!!', command = make_label)

def make_label():
	g.la(text = 'Nice job !')

b1 = g.bu(text = 'Press here', command = make_button)

g.mainloop()
