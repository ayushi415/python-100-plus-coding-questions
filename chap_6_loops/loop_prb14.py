# 2) pattern - numbers triangle

rows = int(input("Enter number of rows: "))
n = 1
for i in range(1, rows + 1):
    for j in range(i):
        print(n, end=" ")
        n += 1
    print()