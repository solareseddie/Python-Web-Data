#
# Scrapes a Web Page to find <a> html tags and click on the nth link
# Uses BeautifulSoup Library
#
# @author (Eddie Solares)
#

import urllib 
from bs4 import BeautifulSoup
#from BeautifulSoup import *

#Asks users to input desired url and opens and reads the page
#To be used for files with similar HTML formatting as 
#"http://python-data.dr-chuck.net/known_by_Remigiusz.html"
url = raw_input('url: ')
pos = int(raw_input('position: '))
num = int(raw_input('number of times: '))
print 'Now looping through links...'

#For loop that iterates a link grab
for i in range(0,num):
	#Opens the url and parses the html
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html, "html.parser")
	
	#Looks for anchor tabs
	tags = soup('a')
	count = 0
	#Add a count to get the desired nth link
	for tag in tags:
		count = count + 1
		#If we reach the count = n, then we print it and make it our new url
		if count == pos:
			print tag.get('href', None)
			url = tag.get('href', None)