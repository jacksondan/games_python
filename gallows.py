
def play():
    print("***************************")
    print("****** Gallows game *******")
    print("***************************")

    key_word = "banana"
    hanged = False
    correct_word = False

    while(not hanged and not correct_word):
        kick = input("Type one word: ")
        for word in key_word:
            print(word)

if(__name__ == "__main__"):
    play()
