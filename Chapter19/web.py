'''import urllib

conn = urllib.urlopen('http://thinkpython.com/secret.html')
for line in conn:
print line.strip()'''

from swampy.Gui import *

g = Gui()
g.title('Web Browser')
canvas = g.ca(width = 400, height = 400)
b1 = g.bu(text = "Click to browse", command = make_change)

