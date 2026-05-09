n = int(input("Enter the no. of rows: "))

for i in range(1, n + 1):
    # Print leading spaces
    print(' ' * (n - i), end='')
    
    # Print stars separated by spaces
    print('* ' * i)