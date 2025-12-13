#Enter a user name and find characters

name = input("Enter a username : ")

if((len(name))<10):
    print("The username contains less than 10 characters")
else:
    print("The username does not contains less than 10 characters")
