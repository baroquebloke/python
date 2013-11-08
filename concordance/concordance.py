# This creates a concordance to the text file specified by the user.
# The cocordance is stored as a dictionary, with the words as keys
# and a list of the line numbers of all lines containing the word as the
# value for each key.

def PrintConcordance(C):
    # This is complete; DON'T CHANGE IT.
    words = C.keys()
    words.sort()
    for w in words:
        print "%-10s appears %d times:" % (w, len(C[w]) )
        print "%10s" % " ",
        count = 0
        for l in C[w]:
            print "%5d" % l,
            count = count + 1
            if count > 9:
                print
                print "%10s" % " ",
                count = 0
        print

def AddWordToConcordance(word, number, C):
    # This does the easy part: it adds to the concordance C
    # the fact that the given word was found on the given line number
    # If the word is already in the dictionary append number onto C[word]
    # otherwise make a new entry: C[word] = [number]
    pass
    
def BuildConcordance(C, fname):
    # This does the hard part:
    # A) It opens the file and reads it one line at a time
    # B) It keeps track of line numbers; each time it reads a new
    #    non-blank line it increments the line counter
    # C) It splits the line into words using a single blank: ' ' as
    #    the delimiter between words.
    # D) It strips punctuation marks, such as "!", ",", ".", "\n" etc.
    #   from words.
    # E) Once the word is stripped of punctuation marks, reduce it to
    #   lower case and send it and its line number to the
    #   AddWordToConcordance() function.
    pass
        
def main():
    # This is complete; DON'T CHANGE IT.
    C = {}
    fileName = raw_input( "file? " )
    try:
        BuildConcordance(C, fileName)
        PrintConcordance(C)
    except IOError:
        print "File not found."
main()
