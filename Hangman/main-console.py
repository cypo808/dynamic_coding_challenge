import random, os, time
from pics import pics
from words import words

# trash, but works :)


pics.reverse()  # inverse pics list for better manipulation

def playagain():
    while True:
        s = str(input("\nDo you want to play again? (y/n): ")).lower()
        if s == "y" or s == "yes":
            play()
            break
        if s == "n" or s == "no":
            print("Okay, see you later :)")
            time.sleep(3)
            exit()
        else:
            print("You probably entered a wrong value...")


def conclusion():
    os.system("cls")  # clean screen
    print("HANGMAN" + "\n" + pics[tries] + "\n" * 2 + word_to_show_string.upper() + "\n")  # print title, 'image' and what you have to guess/already guessed

    won = None
    if word_to_show_string == word_to_guess:
        won = True
    else:
        won = False

    if won:
        print("You won!")
    if not won:
        print("You lost!\nThe word you were looking for was " + word_to_guess.upper())

    playagain()
    

def play():  # run game basically
    global word_to_guess, word_to_show_string, tries
    tries = len(pics) - 1  # set number of tries
    word_to_guess = random.choice(words)  # set the word you are looking for 
    word_to_show = []
    for i in range(len(word_to_guess)):
        word_to_show.append("-")  # this shows on screen
    
    already_guessed_letters = ""

    while tries > 0:  # game loop basically
        word_to_show_string = ""
        for i in word_to_show:
            word_to_show_string += i

        guessed = False

        already_guessed_letters = sorted(already_guessed_letters)
        already_guessed_letters = "".join(already_guessed_letters)

        os.system("cls")  # clean screen
        print("HANGMAN" + "\n" + pics[tries] + "\n" * 2 + word_to_show_string.upper() + "\n\nGuessed letters - " + already_guessed_letters.upper() + "\n")  # print title, 'image' and what you have to guess/already guessed

        while True:
            try:
                user_input = (str(input("Enter a letter: "))[0]).lower()  # get input from user
            except:
                print("You probably entered wrong value...")
            else:
                break

        if user_input not in already_guessed_letters:
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == user_input:
                    word_to_show[i] = user_input
                    word_to_show_string = ""
                    for i in word_to_show:
                        word_to_show_string += i
                    guessed = True
            already_guessed_letters += user_input

        else: 
            print("You already guessed this letter...")
            time.sleep(1.5)
        
        
        if word_to_guess == word_to_show_string:
            break

        if not guessed:
            tries -= 1

    conclusion()    
        

play()
