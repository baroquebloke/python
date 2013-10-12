#this program reads words and prints anagrams

from random import *

def ordering(n):
	new_order = []
	done = False
	while not done:
		number = randint(0, n-1)
		if number in new_order:
			if len(new_order) == n:
				done = True
		elif number not in new_order:
			new_order.append(number)
	return new_order
	

def anagram(w, p):
	new_word = []
	for letter in w:
		letter = letter.index(p)
		new_word.append(letter)
	return new_word

def test():
	done = False
	while not done:
		w = raw_input("Enter a word: ")
		if w == "":
			done = True
		else:
			p = ordering(len(w))
			a = anagram(w, p)
			print p, a
				
test()

