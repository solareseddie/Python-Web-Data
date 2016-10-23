#
# Scrapes a Web Page to find <span> html tags and sum values
# Uses BeautifulSoup Library
#
# @author (Eddie Solares)

import urllib 
from bs4 import BeautifulSoup
#from BeautifulSoup import *

#Asks users to input desired url and opens and reads the page
#To be used for files with similar HTML formatting as 
#"http://python-data.dr-chuck.net/comments_251352.html"
url = raw_input('')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

#Retrieve all of the span tags
tags = soup('span')
sum = 0;

#Sums up the numbers
for tag in tags:
	sum = sum + int(tag.contents[0])
	
print "Sum: ", sum