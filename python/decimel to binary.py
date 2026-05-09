#binary to decimel
decimal_number = int(input("enter a decimel number"))
binary_number = " "
current_number = decimal_number
if current_number == 0:
    binary_number ="0"
else :
    while current_number > 0:
        remainder = current_number%2
        binary_number = str(remainder)+binary_number
        current_number = current_number//2
print(f"The binary equivalent of {decimal_number} is {binary_number}")