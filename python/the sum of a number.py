#Calculate the sum of a number using while loop
import math
x = int(input("Enter a number "))
sum = 0
num = x
while x != 0:
    r = x % 10
    sum = sum + r
    x = x//10
print("The sum of ",num,"is: ",sum)  