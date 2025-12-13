#prime number using while loop and for loop

#while loop
"""num = int(input("Enter a number :"))
i = 2
is_prime = True
if num <= 1:
    is_prime = False
else:
    while i*i <= num:
        if num % i== 0:
            is_prime = False
            break
        i += 1
print(num, "is Prime" if is_prime else "is NOT prime")"""

#for loop
num = int(input("Enter a number :"))
if num <= 1:
    print(f"{num} is not prime number")
else:
    is_prime = True
    for i in range(2,num):
        if num % i== 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not prime number")

