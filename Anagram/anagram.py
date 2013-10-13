#Jacob Farnsworth
#this program reads words and prints anagrams

from random import *

def ordering(n):
    #this generates a random ordering 
    #for a given word, and returns the order
    new_order = []
    done = False
    #I feel this is rather more bloated than it needs to be, 
    #but it seems to work, and I don't want to mess with it
    #since midterms are here...  gah!!!
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
    #ie: Tom may return mot,
    #but mot will never return Tom.
    #come to think of it, the returned anagram will 
    #only ever be lowercase with the way I have this written.
    #I'd love it if we covered this in class...
    for word in word_list:
        lc_word = word.lower()
        p = ordering(len(lc_word))
        a = anagram(lc_word, p)
        if a in word_list and a != lc_word:
            print word, a
main()