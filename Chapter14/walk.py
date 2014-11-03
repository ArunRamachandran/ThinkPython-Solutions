# The fn 'walk' will walks thgrough the directory, prints the names of all 
# the files , and calls itself recursively on all the directories

import os

def walk(dirname):
	for name in os.listdir(dirname):
		path = os.path.join(dirname,name)
		
		if os.path.isfile(path):
			print path
		else:
			walk(path)

cwd = os.getcwd()
print cwd
cw = raw_input('Give a directory : \n')
walk(cw)
