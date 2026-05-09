#Armstrong number
import math
n=int(input("enter the no.= "))
x=n
c=0
sum=0
while n!=0:
    c+=1
    n=n//10
n=x
while n>0:
    rem=n%10
    p=int(pow(rem,c))
    sum=sum+p
    n=n//10
if x==sum:
    print(x,"is a armstrong no.")
else:
    print(x,"is not a armstrong no.")        