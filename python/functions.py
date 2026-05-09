#def hello():  #creating functions
 #   print("Hello, World!")

#hello()

#def sum(a,b):
 #   print(f"sum: {a + b}")

#sum(12,12)    

#keyword arguments
#def hello(name, age):
 #   print(f"Hello, {name}! You are {age} years old.")

#hello(age=25, name="Alice")

#default arguments
#def sum(a,b=45):
 #   print(f"the sum is {a+b}")

#sum(12)

#pallindrom
def pallindrome(st):
    rev = st[::-1]
    if st == rev:
        print(f"{st} is a palindrome")
    else:
        print(f"{st} is not a palindrome")

pallindrome("madam")
pallindrome("hello")

#return functions
def hello():  #creating functions
    return "Hello,swastika!"

print(hello())