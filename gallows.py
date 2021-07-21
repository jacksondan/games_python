
def play():
    print("***************************")
    print("****** Gallows game *******")
    print("***************************")

    key_word = "banana".strip().upper()
    quantity = len(key_word)
    letter_list = []
    hanged = False
    correct_word = False
    chances = 10

    for i in range(0,quantity):
        letter_list.append("_")

    while(not hanged and not correct_word):
        print()
        print("**You have {} chances".format(chances))
        print("Secret Word")
        print(letter_list)

        kick = input("Type one word: ")
        kick = kick.strip().upper()
        found = False
        i = 0
        for letter in key_word:
            if(kick == letter):
                found = True
                letter_list[i] = letter
            i += 1
        if(not found):
            print("Letter doesn't found")
        if(not "_" in letter_list):
            correct_word = True
            print(letter_list)
            print("You got all the letters right !!!")
            print("Congratulations !!!!!!!!")

        chances -= 1
        if(chances == 0 and correct_word == False):
            hanged = True
            print("You hanged yourself")

if(__name__ == "__main__"):
    play()
