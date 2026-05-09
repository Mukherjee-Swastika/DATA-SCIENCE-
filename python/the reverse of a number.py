# print the reverse of a number and using while loop
x = int(input("Enter a number: "))
reversed_x = 0

while x != 0:
    digit = x%10
    reversed_x = reversed_x*10+digit
    x//=10
print("reversed number:" +str(reversed_x))    
