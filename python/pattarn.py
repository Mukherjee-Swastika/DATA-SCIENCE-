n = int(input("Enter a range: "))
for i in range(n):
    print(" "*(n-i),end="")
    for j in range(i+1):
        print("*",end="")
    print()   