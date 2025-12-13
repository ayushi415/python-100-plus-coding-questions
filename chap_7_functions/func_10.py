# print first n lines of the following pattern
#  * * *
#  * *
#  *

def patterns(n):
    for i in range(n,0,-1):
        print("*" * i)
n = int(input("enter number of rows :"))
print(patterns(n))