def computepay(h, r) :
    print("In computepay", h, r)
    if h > 40:
        reg = r * h
        opt = (h - 40.0) * (r * 0.5)
        pay = reg + opt
    else:
        pay = fh * fr
    return pay
sh = input('Enter hours: ')
sr = input('Enter rate: ')
fh = float(sh)
fr = float(sr)
xp = computepay(fh, fr);

print ("Pay: ", xp)
