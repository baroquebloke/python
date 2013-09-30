#this finds palindromes in words.txt, prints them, then prints the total number of words and total number of palindromes



def main():
	
	word_count = 0
	pal_count = 0

	file = open("words.txt", "r")
	for line in file:
		word = line.strip()
		lc_word = word.lower()
		word_count = word_count + 1
		reverse = ""
		for letter in lc_word:
			reverse = letter + reverse
		if lc_word == reverse:
			print word
			pal_count = pal_count + 1
		
	
	print ("Out of the %s words in this file, %s were palindromes") % (word_count, pal_count)

main()