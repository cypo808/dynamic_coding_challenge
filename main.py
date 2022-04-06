import os, csv, time

dictionary = {}

with open("data.csv", "r", newline="") as file:
    reader = csv.reader(file)
    for line in reader:
        dictionary[line[0]] = line[1]


def main():
    os.system("cls")
    print("Contact Book\nType \"h\" for help")
    while True:
        # u = user - input from user
        u = str(input(">>> ")).lower()   
        if u == "h" or u == "help" or u == "?":
            help()
        if u == "s" or u == "show":
            show()
        if u == "a" or u == "add":
            add()
        if u == "d" or u == "delete":
            delete()
        if u == "e" or u == "exit":
            exit_program()
        if u not in "hsade":
            print("Unknown command... type \"h\" for help")


def help():
    print("h - help - shows this screen")
    print("s - show - shows your contacts")
    print("a - add - add new contact")
    print("d - delete - delete contact")
    print("e - exit - exit program\n")

def show():
    if bool(dictionary):
        for i in dictionary:
            print("Name: " + i)
            print("Phone: " + dictionary[i])
    if not bool(dictionary):
        print("Your Contact Book in empty!\nEnter \"a\" to add new contact")

def add():
    name = str(input("Enter name of new contact: "))
    phone = str(input("Enter phone for " + name + ": "))
    dictionary[name] = phone

def delete():
    try:
        userinput = str(input("Which contact do you want to delete?: "))
        del dictionary[userinput]
    except KeyError:
        print("This contact doesn't exits")

def exit_program():
    while True:
        u = str(input("Do you want to save changes? (y/n): ")).lower()
        if u == "y" or u == "yes":
            with open("data.csv", "w", newline="") as file:
                writer = csv.writer(file)
                for i in dictionary:
                    writer.writerow([i, dictionary[i]])
            break
        if u == "n" or u == "n":
            break
        else:
            print("You probably entered a wrong value...")
            
    print("Okay, see you later :)")
    time.sleep(2)
    exit()


main()
