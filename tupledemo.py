print("Demonststion of Tuple")

#Data : Hetrogeneous
#Ordered : Yes
#Indexed : Yes
#Mutable : No
#Duplicates : Yes


data=(11,21,51,101,21,11)
data1=(11,90.88,True,"Hello") #heterogenous

print("Data is Heterogenous : ",data1)
print("Data is ordered : ",data1)
print("Data at index 2 : ",data1[2])
print("Data with duplicate elememts : ",data)

print("List is mutable")
data.append(201)
print("Data after append",data)
data.pop()
print("Data after pop",data)

