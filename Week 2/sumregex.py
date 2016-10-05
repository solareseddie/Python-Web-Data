#Uses Regex code to look for all the numbers in the text file

import re

hand = open('regex_sum_251347.txt')
numlist = []

#Loops through each line
for line in hand:
	line = line.rstrip()
	#Regex code to find all numbers in text
	y = re.findall('[0-9]+', line)
	#Appends each number to the list
	if len(y) != 0:
		for i in range(0, len(y)):
			numlist.append(y[i])

#Converts strings to ints and prints
numlist = [int(i) for i in numlist]
print sum(numlist)