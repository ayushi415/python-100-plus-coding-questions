#A program to find the greatest of four numbers entered by the user

'''a=int(input("Enter number a:"))
b=int(input("Enter number b:"))
c=int(input("Enter number c:"))
d=int(input("Enter number d:"))'''
a=12
b=123
c=543 
d=99

if(a>b and a>c and a>d):
    print("a is greater")
elif(b>a and b>c and b>d):
    print("b is greater")
elif(c>a and c>b and c>d):
    print("c is greater")
else:
    print("d is greater")    


