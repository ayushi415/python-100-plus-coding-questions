# user input a number

num = int(input("Enter a number : "))

if num > 0:
    if num % 2 == 0: 
        print("Multiplication with 2.5: ",num * 2.5)
    else:
        print("Addition with 10: ",num + 10)
elif num < 0:
     if num % 2 == 0:
        print("Divided by 2.5: ",num / 2.5)
     else:
        print("Subtraction with 5: ",num - 5)
else:
    print("Number is Zero")        

