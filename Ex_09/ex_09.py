fname = input("Enter the file: ")
if len(fname) < 1:
    fname = "clown.txt"
hand = open(fname)

di = dict()
for line in hand:
    line = line.rstrip()
    #print(line)
    words = line.split()
    #print(words)
    for word in words:

        """
        print(word)
        if word in di:
            di[word] = di[word] + 1
            print("**EXISTING ITEM**")
        else:
            di[word] = 1
            print("**NEW ITEM**")
        print(di[word])
        """
        """
        But all this could be done in one line
        #If key is not in dictionarie, returns zero
        oldcount = di.get(word, 0)
        print(word,"old",oldcount)
        newcount = oldcount + 1
        di[word] = newcount
        print(word,"new",newcount)
        """
        #idiom: retrieve, create, update counter
        di[word] = di.get(word, 0) + 1
        #print(word,"new",di[word])
print(di)

#Find the most common words
largestnum = -1
mostrepword = None
for k, v in di.items():
    if v > largestnum:
        largestnum = v
        mostrepword = k # captures and remember the largest number
print("Done",mostrepword,largestnum)
