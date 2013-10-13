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
    word = []
    for i in p:
        x = w[i]
        word.append(x)
    return ''.join(word)


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