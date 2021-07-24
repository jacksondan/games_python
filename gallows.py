import random
def play():
    __presentation()
    key_word = __key_word_generator()
    letter_list = __empty_spaces_generator(key_word)

    hanged = False
    correct_word = False
    errors = 0

    while(not hanged and not correct_word):
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
            errors += 1
            __gallows_drawing(errors)

        if(not "_" in letter_list):
            correct_word = True
            __you_win_message(letter_list)

        if(errors == 7 and correct_word == False):
            hanged = True
            __you_lose_message(key_word)


def __presentation():
    print("***************************")
    print("****** Gallows game *******")
    print("***************************")

def __key_word_generator():
    file = open("files/key_words.txt", "r")
    key_word_list = [line for line in file]
    key_index = random.randrange(0, len(key_word_list))
    file.close()
    key_word = key_word_list[key_index].strip().upper()
    return key_word

def __empty_spaces_generator(key_word):
    return ["_" for letter in key_word]

def __you_lose_message(key_word):
    print("\nMy goodness, You're hanged!")
    print("The key word was '{}'".format(key_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def __you_win_message(letter_list):
    print()
    print(letter_list)
    print("You got all the letters right !!!")
    print("Congratulations !!!!!!!!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def __gallows_drawing(errors):
    print("  _______     ")
    print(" |/      |    ")

    if(errors == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(errors == 2):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    if(errors == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(errors == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(errors == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(errors == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (errors == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
if(__name__ == "__main__"):
    play()

# inteiros = [1,3,4,5,7,8,9]
# pares = [x for x in inteiros if x % 2 == 0]

 #   @property
 #   def salario(self):
 #       return self.__salario

#    @salario.setter
#    def salario(self, novo_salario):
#        raise ValueError("Impossivel alterar salario diretamente. Use a funcao calcula_salario().")
