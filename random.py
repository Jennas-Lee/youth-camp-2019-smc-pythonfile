"""
Date        : 2019.07.16
School      : Semyung Computer High School
Team        : SemyungSe~myung
Member      : Seoyun Kim, Hyunjun Yun, Seungjun Lee
File name   : random.py
Used Editor : Vim
"""

import random						# Get random module

min = raw_input("Min : ")				# min -> Get minimum number
max = raw_input("Max : ")				# max -> Get maximum number

i = randint(min, max)					# i -> random number between min and max

while(1):
	num = raw_input("Plz Enter a Number : ")	# num -> Get a answer number
	if(num <= max ):				# min <= num <= max
		if(num > i):				# num > i
			print("too high!")
		elif(num == i):				# num = i
			print("Answer!")
			break				# Finish this program
		else:					# num < i
			print("too lower!")
	else:						# min >= num or num >= max
		print("Not in Range")
