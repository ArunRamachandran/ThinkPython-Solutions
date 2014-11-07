import swampy
from swampy.TurtleWorld import *

class SimpleTurtleWorld(TurtleWorld):
	'''This class is identical to turltle world '''
	def setup(self):
		''' set up is the fn that creates and re-arranges the 
		widgets '''
		self.row()
		''' this  code willc reate the Canvas and the column frame,
		according the picture '''
		self.canvas = self.ca(width = 400, height = 400, bg = 'white')
		col()
		
		self.gr(cols = 2)
		self.bu(text = 'Print Canvas', command = self.canvas.dump)
		self.bu(text = 'Quit', command = self.quit)
		self.bu(text = 'Make Turtle', command = self.make_turtle)
		self.bu(text = 'Clear', command = self.clear)
		self.endgr()

		self.row([0,1], pady = 30)
		self.bu(text = 'Run File', command = self.run_file)
		self.en_file = self.en(text = 'snowflake.py', width = 5)
		self.endrow()

		def run_file(self):
			filename = self.en_file.get()
			fp = open(filename)
			source = fp.read()
			self.inter.run_code(source, filename)

		self.te_code = self.te(width = 25, height = 10)
		self.te_code.insert(END, 'world.clear()\n')
		self.te_code.insert(END, 'bob = Turtle(world)\n')
		
		self.bu(text = 'Run code', command = self.run_text)

		def run_text():
			source = self.te_code.get(1.0, END)
			self.inter.run_code(source, '<user-provided code>')

	
sample = SimpleTurtleWorld()
print sample	
