#sum of first n natural number

#for loop
n = int(input("Enter number : "))
total = 0
for i in range(1,n+1):
    total += i
print(f"Sum of first {n} natural numbers is : {total}")


#while loop
n = int(input("Enter number : "))
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print(f"Sum of first {n} natural numbers is : {total}")

