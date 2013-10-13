#this program reads words and prints anagrams

from random import *

def ordering(n):
    #this generates a random ordering 
    #for a given word, and returns the order
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
    #this takes the aforementioned 
    #random order and the word and reorders 
    #the letters in the new order
    word = []
    for i in p:
        x = w[i]
        word.append(x)
    return ''.join(word)

def main():
    #this opens a word file and reads the words into a list.
    #The list is then passed through the two functions above 
    #to find and print anagrams in the list
    word_list = []
    file = open("words.txt", "r")
    for line in file:
        word_list.append(line.strip())
    #case recognition only partially works.  
    #ie: program will print "Edna edna"
    ############ as well as "Edna dean"
    for word in word_list:
        lc_word = word.lower()
        p = ordering(len(lc_word))
        a = anagram(lc_word, p)
        if a in word_list and a != word:
            print word, a
main()