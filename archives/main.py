import random, math, time, os

'''
min, max = range of numbers to guess
guessed_number = it's pretty obvious
tries = number of tries for player to guess
n = number, that player guessed
playagain = if player want to play again
i = basically number of try
'''

def main():
    os.system("cls") # clean screen at beginning
    print("NUMBER GUESSING GAME")

    while True: # getting lower bound
        try:
            min = int(input("Enter lower bound: "))
        except ValueError:
            print("You probably didn't enter a number, try again...")
        except:
            print("Something went wrong...")
        else:
            break
    while True: # getting higher bound
        try:
            max = int(input("Enter higher bound: "))
        except ValueError:
            print("You probably didn't enter a number, try again...")
        except:
            print("Something went wrong...")
        if max > min:
            break
    
    guessed_number = random.randint(min, max)
    tries = round(math.log(max - min + 1, 2)) # i stole this from somewhere
    print("You have " + str(tries) + " tries")
    won = None
    i = 1

    while tries > 0: # game loop 
        while True: # getting number from player  
            try:
                n = int(input("\n" + str(i) + ". Guess a number: "))
            except ValueError:
                print("You probably didn't enter a number, try again...")
            except:
                print("Something went wrong...")
            else:
                break

        if n == guessed_number:
            won = True
            break
        if n > guessed_number:
            print("Your guess was too high")
        if n < guessed_number:
            print("Your guess was too low")

        tries -= 1
        i += 1

    # after game, if player won or lost
    if won:
        print("\nYou won!")
    if not won:
            print("\nYou lost!\nThe number you were looking for was " + str(guessed_number))


    while True: # play again
        playagain = input("\nDo you want to play again? ").lower()

        if playagain == "yes" or playagain == "y":
            main()
            break
        if playagain == "no" or playagain == "n":
            print("Okay, see you later!")
            time.sleep(3)
            break
        else:
            print("You probably entered something wrong, try again...")
        
main()
