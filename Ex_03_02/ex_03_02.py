print("vamoa programar")
sh = input("Enter hours: ")
sr = input("Enter rate: ")
try:
    fh = float(sh)
    fr = float(sr)
    if fh > 40:
        reg = fr * fh
        otp = (fh - 40) * (fr * 0.5)
        xp = reg + opt
    else:
        xp = fh * fr
    print("Pay :", xp)
except:
    print("Ups that's not a number, try again")
