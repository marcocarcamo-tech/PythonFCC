print("terminal test")
hours = input('Enter hours: ')
rate = input('Enter rate: ')
if int(hours) > 40:
    spetialhours = (int(hours) - 40)
    spetialrate = float(rate) * 1.5
    hours=40
    pay = (float(hours) * float(rate)) + (float(spetialhours) * float(spetialrate))
else:
    pay = float(hours) * float(rate)
print(pay)
