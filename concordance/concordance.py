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
    if word in C:
        C[word].append(number) 
    else:
        C[word] = [number]
    
    
def BuildConcordance(C, fname):
    line_count = 0
    file = open(fname, "r")
    for line in file:
        line = line.strip()
        if line != "":
            line_count = line_count + 1    
        for word in line.split():  
            word = word.strip("][.,';:-_|}{~`<>/+=@#$%^&*")
            word = word.strip("\n")
            word = word.strip('?"!"')
            if word != "":
                word = word.lower()
                AddWordToConcordance(word, line_count, C)

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
