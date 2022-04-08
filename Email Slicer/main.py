userinput = str(input("Enter your email: ")).strip()  # .strip() to remove unwanted spaces aroud variable
username = userinput[:userinput.index('@')]  # find @ and remove everything before it
domain = userinput[userinput.index('@') + 1:]  # find @ and remove everything 1 character after if 

print("Username - " + username)
print("Domain - " + domain)
