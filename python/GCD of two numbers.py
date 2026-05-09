#GCD of two numbers
a = int(input("Enter the 1st No.= "))
b = int(input("Enter the 2nd No.= "))
i=1
while (i<=a and i<=b):
    if(a%i==0 and b%i==0):
        GCD=i
    i=i+1
print("GCD is:",GCD)                