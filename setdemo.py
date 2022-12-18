print("Demonststion of Tuple")

#Data : Hetrogeneous
#Ordered : Yes
#Indexed : Yes
#Mutable : Yes
#Duplicates : Yes


data={11,21,51,101,21,11}
data1={11,90.88,True,"Hello"} #heterogenous

print("Data is Heterogenous : ",data1)
print("Data is ordered : ",data1)
#print("Data at index 2 : ",data1[2])
print("Data with duplicate elememts : ",data)

print("set is mutable")

data.add(211)
print("Data after addition : ",data)

data.remove(211) #it will remove element only when it is there
print("Data after removal : ",data)

data.discard(201)  #remove when there or else if no there it will no give error
print("Data after Discard : ",data)

