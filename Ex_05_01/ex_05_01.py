# Variables
done = "done"
sum = 0
count = 0
average = 0
lastnumber = 0
# Loop wich evaluates input for numbers, "done", or invalid input
while True:
    newnumber = input("Enter a number: ")
    try:
        if newnumber == "done":
            break
        else:
            newnumber = int(newnumber)
            sum = lastnumber + newnumber
            count = count + 1
            lastnumber = sum
            average = sum/count
    except:
        print("Respuesta inválida")
#Results for total, average, count
print("El total es: ", sum)
print("El promedio es: ", average)
print("La cantidad de números introducidos es: ", count)
