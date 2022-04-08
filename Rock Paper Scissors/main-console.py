import os, random, time

list = ["r", "p", "s"]
max_score = 3

def main():
    user_score = 0
    pc_score = 0

    os.system("cls")
    print("ROCK, PAPER, SCISSORS\nYou will be playing against PC, the first to win " + str(max_score) + " times wins!")

    while True:
        result = None
        while True:
            user = str(input("\nRock, paper, scissors: "))[0].lower()
            if user not in "rps":
                print("You can't play with that :)")
            else:
                break
        pc = random.choice(list)

        if user == "r":
            if pc == "r":
                result = "draw"
            if pc == "p":
                result = "lost"
            if pc == "s":
                result = "won"
        if user == "p":
            if pc == "r":
                result = "won"
            if pc == "p":
                result = "draw"
            if pc == "s":
                result = "lost"
        if user == "s":
            if pc == "r":
                result = "lost"
            if pc == "p":
                result = "won"
            if pc == "s":
                result = "draw"
        
        if result == "won":
            print("You won")
            user_score += 1
        if result == "lost":
            print("You lost")
            pc_score += 1
        if result == "draw":
            print("It's draw")

        print("Score - " + str(user_score) + " : " + str(pc_score))
    
        if user_score >= max_score or pc_score >= max_score:
            break

    if user_score > pc_score:
        print("\nYOU WON!")
    if user_score < pc_score:
        print("\nYOU LOST!")
    print("The final score was " + str(user_score) + " : " + str(pc_score))

    while True:
        playagain = str(input("Do you want to play again? (y/n): "))[0].lower()
        if playagain == "y":
            main()
        if playagain == "n":
            print("Okay, see you later :)")
            time.sleep(2)
            exit()
        else:
            print("I don't understand...")


main()
