#Program tha takes a slice from a string and converts it to a float.
#Directly
str = "X-DSPAM-Confidence: 0.8475"
strf = str.find("0")
print(strf)
strsl = str[20: ]
print(strsl)
strtonum = float(strsl)
print(strtonum)
#indirectly, from space, but it could also be from colon"
str = "X-DSPAM-Confidence: 0.8475"
strf = str.find(" ")
print(strf)
strsl = str[strf + 1: ]
print(strsl)
strtonum = float(strsl)
print(strtonum)
