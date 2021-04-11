#Personal solution
file = open('mbox-short.txt')
for line in file:
    line = line.rstrip()
    line = line.upper()
    print(line)
#Course solution
"""
fh = open('mbox-short.txt')

for lx in fh:
    ly = lx.rsrip()
    print(ly.upper())
"""
