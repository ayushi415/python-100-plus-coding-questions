# greatest of 3 numbers

def gretest_number(a,b,c):
    if a>b and a>c:
        print("a is greater")
    elif b>a and b>c:
        print("b is greatest")
    else:
        print("c is greatest")       
print(gretest_number(23,99,54))