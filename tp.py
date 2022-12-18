
list1=[3,4,5,6,7,8]
list2=[]

for no in list1:
    c = 0
    for i in range(2,no):
        if no % i == 0:
            c+=1
    if c==0:
        list2.append(no)


print(list2)
