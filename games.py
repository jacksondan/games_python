import divination
print("************************")
print("******* Welcome ********")
print("*** Choose your game ***")
print("************************")

choice = int(input("(1) Divination, (2) Game Two: "))

if(choice == 1):
    divination.play()
elif(choice == 2):
    print("Game 02")
else:
    print("Choice invalid")