import time, datetime

class T:  # time - current time
    def __init__(self):
        self.input = time.gmtime()
        self.year = self.input.tm_year
        self.month = self.input.tm_mon
        self.day = self.input.tm_mday
        # time from epoch [sec]
        self.value = int(datetime.datetime(self.year, self.month, self.day).timestamp())

class U:  # user - birthday of user
    def __init__(self):
        while True:
            try:
                self.input = input("Enter your birth date (DD MM YYYY): ").split()
            except:
                print("You probably entered wrong date...")
            else:
                break
        
        self.year = int(self.input[2])
        self.month = int(self.input[1])
        self.day = int(self.input[0])
        # time from epoch [sec]
        try:
            self.value = int(datetime.datetime(self.year, self.month, self.day).timestamp())
        except OSError:
            self.value = None

class F:
    def __init__(self):
        if not u.value == None:
            self.value = int(t.value - u.value)
            self.sec = self.value
            self.min = int(self.sec / 60)
            self.hour = int(self.min / 60)
            self.day = int(self.hour / 24)
            self.month = int(self.day / (365 / 12))
            self.year = int(self.day / 365)
        else:
            self.value = None

t = T()
u = U()
f = F()


def results():
    try:
        if f.value > 1:
            print("You are " + str(f.year) + " year(s) old")
            print("You are " + str(f.month) + " month(s) old")
            print("You are " + str(f.day) + " day(s) old")
            print("You are " + str(f.hour) + " hour(s) old")
            print("You are " + str(f.min) + " minute(s) old")
            print("You are " + str(f.sec) + " second(s) old")
        if f.value < 1:
            print("You will be born in " + str(abs(f.year)) + " year(s)")
            print("You will be born in " + str(abs(f.month)) + " month(s)")
            print("You will be born in " + str(abs(f.day)) + " day(s)")
            print("You will be born in " + str(abs(f.hour)) + " hour(s)")
            print("You will be born in " + str(abs(f.min)) + " minute(s)")
            print("You will be born in " + str(abs(f.sec)) + " second(s)")
        if f.value == 0:
            print("You will be born today!")
    except TypeError:
        print("Error... OS can't calculate your birthdate, because you were born before epoch")

results()
input()
