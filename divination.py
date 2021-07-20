import random
def play():
    print("***************************")
    print("** Guess what the number **")
    print("***************************")

    secret_number = random.randrange(1,101)
    continue_game =True
    attempts = 1

    while(continue_game):
        print("Attempt: {}".format(attempts))
        kick = int(input("Text your number between 1 and 100: "))

        if(kick < 1 or kick > 100 ):
            print("you type a illegal number")
            continue

        right_answer = kick == secret_number
        bigger = kick > secret_number
        smaller = kick < secret_number

        if(right_answer):
            print("Your're right! Congratulations!!!!!!!!")
            print("Quantities of attempts: {}".format(attempts))
            break
        else:
            if(bigger):
                print("You failed! Your kick was bigger than the secret number")
            elif(smaller):
                print("You failed! Your kick was smaller than the secret number")
        print("Try again")
        attempts += 1
if(__name__ == "__main__"):
    play()
    #for rodada in range(1,11): for comum
    #   print("Teste for",rodada)
    #for rodada in range(1,11,2): O último valor define o valor a ser incrementado
    #   print("Teste for",rodada)

    #for rodada in [1,3,5,6,7,9]]: Pode ser adicionado um arrey para ser iterado
    #   print("Teste for",rodada)
