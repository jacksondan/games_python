print("*********************")
print("guess what the number")
print("*********************")

secret_number = 42
continue_game =True
attempts = 1

while(continue_game):
    print("Quantities of attempts: {}".format(attempts))
    kick = int(input("Text your number: "))

    right_answer = kick == secret_number
    bigger = kick > secret_number
    smaller = kick < secret_number

    if(right_answer):
        print("Your're right! Congratulations")
        print("Quantities of attempts: {}".format(attempts))
        continue_game = False
    else:
        if(bigger):
            print("You failed! Your kick was bigger than the secret number")
        elif(smaller):
            print("You failed! Your kick was smaller than the secret number")
        print("Try again")
    attempts += 1
