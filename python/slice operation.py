#slice operation
li=[]
n=int(input("Enter the Range = "))
for i in range(0,n,1):
    li.append(input("Enter the String = "))
print('List = ',li)
x=slice(2)  #[0:1]
print(li[x])
x=slice(2,5)
print(li[x])
x=slice(0,6,2)
print(li[x])