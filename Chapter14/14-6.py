# The 'urlib' module provides methods for manipulating URLSs and downloading
# information from the web. The following downloads and prints a secret 
# message from 'thinkpython.com'

import urllib

conn = urllib.urlopen('http://thinkpython.com/secret.html')
for line in conn:
	print line.strip()


