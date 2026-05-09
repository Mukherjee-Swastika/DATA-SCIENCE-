n = 6  # This is the number of rows in the first (increasing) half of the pattern

# Print the increasing part of the pattern
for i in range(1, n + 1):
    print("* " * i)

# Print the decreasing part of the pattern
for i in range(n - 1, 0, -1):
    print("* " * i)