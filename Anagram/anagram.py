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
    #I'm supposed to have a loop for this function that runs through p, and for each index in p, put that entry of word in the result...
    zip_list = zip(p, w)
    zip_list.sort()
    result = [x[1] for x in zip_list]

    return result


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