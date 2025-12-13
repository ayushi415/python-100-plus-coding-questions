#factorial of a number:

#for loop
n = int(input("Enter number :"))
fact = 1
for i in range(1,n + 1):
    fact *= i
print("Factorial of",n , "is",fact)


#while loop

num = 5
fact = 1
i = 1
while i<= num:
    fact *= i
    i += 1
print("Factorial of",num , "is",fact)