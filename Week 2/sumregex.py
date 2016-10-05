import re

hand = open('regex_sum_251347.txt')
numlist = []
for line in hand:
	line = line.rstrip()
	y = re.findall('[0-9]+', line)
	if len(y) != 0:
		for i in range(0, len(y)):
			numlist.append(y[i])

#print numlist
numlist = [int(i) for i in numlist]
print sum(numlist)