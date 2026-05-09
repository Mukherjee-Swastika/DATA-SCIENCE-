# count the number of uppercase,lowercase and numbers entered by the users.
def count_characters():
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    
    while True:
        char = input("Enter a character (or '*' to stop): ")
        
        if char == '*':
            break
        
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            print("Invalid input. Please enter a single character.")
    
    return uppercase_count, lowercase_count, digit_count

# Example usage
uppercase, lowercase, digits = count_characters()
print(f"Uppercase letters: {uppercase}")
print(f"Lowercase letters: {lowercase}")
print(f"Digits: {digits}")
