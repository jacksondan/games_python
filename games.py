import divination
import gallows
print("************************")
print("******* Welcome ********")
print("*** Choose your game ***")
print("************************")

choice = int(input("(1) Divination, (2) Gallows: "))

if(choice == 1):
    divination.play()
elif(choice == 2):
    gallows.play()
else:
    print("Choice invalid")