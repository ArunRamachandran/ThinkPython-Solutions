# 14-4 --- 1.
# Write a program that searches a directory and all of its 
#subdirectories, recursively, and returns a list of complete 
#paths for all files with a given suffix.

import os

def get_files(dirname):
	for name in os.listdir(dirname):
		path = os.path.join(dirname,name)
		
		if os.path.isfile(path):
			copy = path
			name,ext = path.split('.')
			if ext == 'py':
				print path
			else:
				pass
		else:
			get_files(path)
		

print "Looking for files with '.py' extension"
cw = raw_input('Give directory ?\n')
print "All files with extension '.py' : "
get_files(cw)

