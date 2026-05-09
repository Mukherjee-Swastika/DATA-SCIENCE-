# Store positive & negative element in 2 separate list
li=[]
lipos=[]
lineg=[]
cpos=0
cneg=0
n=int(input("Enter the Range = "))
for i in range(0,n,1):
    li.append(int(input("Enter the No. = ")))
print("List = ",li)# [10,-5,17,13]
for i in li:
    if i>0:
        lipos.append(i)
        cpos+=1
    elif i<0:
        lineg.append(i)
        cneg+=1
print("Positive List = ",lipos,"Total Positive Element = ",cpos)
print("Negative List = ",lineg,"Total Negative Element = ",cneg)