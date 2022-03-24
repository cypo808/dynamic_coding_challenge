import random, os, time

'''
TODO
one lil problem - when there are same letters more times in a word, it recognises just the first letter... need to fix it somehow
'''

pics = ["""
 +---+
     |
     |
     |
    ===""", """
 +---+
 O   |
     |
     |
    ===""", """
 +---+
 O   |
 |   |
     |
    ===""", """
 +---+
 O   |
/|   |
     |
    ===""", """
 +---+
 O   |
/|\  |
     |
    ===""", """
 +---+
 O   |
/|\  |
/    |
    ===""", """
 +---+
 O   |
/|\  |
/ \  |
    ==="""]

list = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple', 'pink', 'white', 'gray', 'black']

dict = {}


def draw(n):
    os.system("cls")
    print("HANGMAN")
    print(pics[n - 1])
    print("")
    show_text = ""
    for i in range(len(dict)):
        show_text += dict[i]
    print(show_text)
    print(word)


def gameover():
    if lost:
        draw(len(pics))
        print("\nYOU LOST!")
        print("\nThe word you were looking for was \"" + word + "\"")
    if not lost:
        print("YOU WON!")



def main():
    global word, tries, lost
    word = random.choice(list).upper()
    tries = 6
    lost = False
    guessed = ""

    for i in range(len(word)):
        dict[i] = "_"
    

    while not lost:
        draw(len(pics) - tries)
        
        user_input = input("\nEnter a letter: ").upper()

        for i in range(len(word)):
            if user_input in word: # if player guesses some letter
                dict[word.find(user_input)] = user_input
            else:
                tries -= 1

        guessed = ""
        for i in range(len(dict)):
            guessed += dict[i]
        print("GUESSED: " + guessed)

        #time.sleep(3)

        
        if tries == 0:
            lost = True
        if guessed == word:
            break

        gameover()

main()

