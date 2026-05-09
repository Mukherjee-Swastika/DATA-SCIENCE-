# Define the size of the pattern
n = 5  # This is the number of rows in the top half of the pattern

# Print the top half of the pattern
for i in range(n):
    # Print leading spaces
    print(" " * (n - i - 1), end="")
    # Print stars
    print("*" * (2 * i + 1))

# Print the bottom half of the pattern
for i in range(n - 2, -1, -1):
    # Print leading spaces
    print(" " * (n - i - 1), end="")
    # Print stars
    print("*" * (2 * i + 1))