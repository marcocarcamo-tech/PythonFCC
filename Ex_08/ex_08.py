#This program finds lines which starts with "From" and then extract the third element
han = open("mbox-short.txt")

for line in han:
    line = line.rstrip()
    words = line.split()
    #We creat a guardian in case there´s an empty line or ther´s not a word [2]
    if  len(words) < 3:
        continue
    elif words[0] != "From":
        continue
    print(words[2])
