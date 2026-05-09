#a = [12,30,60,35,67]


#for i in range(len(a)):
 #   print(a[i])

    #2nd way

#for i in a:
 #   print(i)


#list append
#a = [12,30,60,35,67]
#a.append(100)
#print(a)

#insert
#a.insert(2,100)
#remove
#a.remove(a[2])
#change
#a[2] = 100
#print(a)




#avg
#l = [20,30,10,40,50]
#sum = 0
#for i in l:
 #   sum = sum + i
#print("the average is:", sum/len(l))



#largest
l = [20,30,10,40,50]
largest = l[0]
index = 0

for i in range(len(l)):
    if l[i] > largest:
        largest = l[i]
        index = i

print("The largest element is:", largest)
print("The index of the largest element is:", index)