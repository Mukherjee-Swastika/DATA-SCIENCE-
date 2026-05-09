#binary to decimal number using while
binary_number = int(input("Enter a binary_number: "))
decimal_number = 0
index = 0
while binary_number != 0:
    last_digit = binary_number % 10 
    decimal_number += last_digit * pow(2,index)
    binary_number = binary_number // 10
    index = index + 1

print("The decimal_number is: ",decimal_number)    