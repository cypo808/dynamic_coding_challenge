import os, csv, time

dictionary = {}

with open("data.csv", "r", newline="") as file:
    reader = csv.reader(file)
    for line in reader:
        dictionary[line[0]] = line[1]


def main():
    os.system("cls")
    print("Contact Book\n")
    if bool(dictionary): 
        show()

    print("\nType \"h\" for help")
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
    print("Contact added!\n")

def delete():
    try:
        userinput = str(input("Which contact do you want to delete?: "))
        del dictionary[userinput]
    except KeyError:
        print("This contact doesn't exits")
    else:
        print("Contact deleted!")

def exit_program():
    global x
    x = None
    while True:
        u = str(input("Do you want to save changes? (y/n/cancel): ")).lower()
        if u == "y" or u == "yes":
            with open("data.csv", "w", newline="") as file:
                writer = csv.writer(file)
                for i in dictionary:
                    writer.writerow([i, dictionary[i]])
            x = True
            break
        if u == "n" or u == "no":
            x = True
            break
        if u == "c" or u == "cancel":
            x = False
            break
        else:
            print("You probably entered a wrong value...")

    if x:
        print("Okay, see you later :)")
        time.sleep(2)
        exit()


main()
