"""
for i in range(1,5):
    print(i,end=" ")

for i in range(1,10,2):
    print(i,end=" ")
"""

"""
values=[10,20,30,40,50]

print(values[0])
print(values[1])
print(values[2])
print(values[3])
print(values[4])
print()
for i in range(0,len(values)):
    print(values[i])

print()

for no in values:
    print(no)
"""



def main():
    list1=list()  # object of list class
    listsize=int(input("How many values do you want in list : "))
    i=0
    """ 
    while(i<listsize):
        val=int(input(f"Enter the number at index {i}  : "))
        list1.append(val)  #list1.insert(i,val)
        i=i+1
    """
    for i in range(listsize):
        val=int(input(f"Enter the number at index {i}  : "))
        list1.append(val)  #list1.insert(i,val)

    print(list1)

if __name__=="__main__":
    main()
