
def play():
    print("***************************")
    print("****** Gallows game *******")
    print("***************************")

    key_word = "banana"
    quantity = len(key_word)
    print(quantity)
    hanged = False
    correct_word = False

    while(not hanged and not correct_word):
        kick = input("Type one word: ")
        kick = kick.strip()
        found = False
        i = 0

        for letter in key_word:
            if(kick.lower() == letter.lower()):
                found = True
                print("*** Letter {} was found on index {}".format(letter,i) )
            i += 1
        if(not found):
            print("Letter doesn't found")

if(__name__ == "__main__"):
    play()
