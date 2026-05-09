# calculate the average of first n natural numbers 
x = int(input("Enter a number: "))
sum = 0
avg = 0
for i in range(1,x+1):
    sum = sum+i
avg = sum/x
print("The sum of the n natural number is: ",sum)
print("The avarage of the n natural numbers is: ",avg)