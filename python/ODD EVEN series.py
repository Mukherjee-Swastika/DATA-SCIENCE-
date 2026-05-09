# print all the numbers from m-n thereby classify them as even or odd using for loop.
n = int(input("Enter a number: "))
print("-----------------------------")
print("\tODD\tEVEN")
print("-----------------------------")
for i in range(1, n+1,1):
    if i%2==0:
        print("/t",i)
    else :
        print("/t",i,end=" ")    