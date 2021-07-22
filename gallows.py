import random
def play():
    print("***************************")
    print("****** Gallows game *******")
    print("***************************")

    file = open("files/key_words.txt","r")
    key_word_list = [line for line in file]
    key_index = random.randrange(0,len(key_word_list))
    file.close()

    key_word = key_word_list[key_index].strip().upper()
    letter_list = ["_" for letter in key_word]
    hanged = False
    correct_word = False
    chances = 10

    while(not hanged and not correct_word):
        print("\n**You have {} chances".format(chances))
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

# inteiros = [1,3,4,5,7,8,9]
# pares = [x for x in inteiros if x % 2 == 0]
