# Written by Anil & Khuong

import time

while True:
	for x in range (0,10):
		text = '-' * x
		text += '#'
		remaining = 9 - x
		text += '-' * remaining
		print (text, end="\r")
		time.sleep(0.5)

	for x in range (1,9):
		first = 9 - x
		second = x
		text = '-' * first + '#' + '-' * second
		print (text, end="\r")
		time.sleep(0.5)