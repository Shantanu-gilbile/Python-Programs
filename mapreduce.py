def main():
    list1=list()
    list2=list()
    list3=list()

    no =int(input("Enter the number of values  :"))

    for i in range(0,no):
        no1=int(input("Enter the number : "))
        list1.append(no1)
    print(list1)

    print("Initial list : ",list1)

    #filter
    for no in list1:
        if no % 2==0 :
            list2.append(no)

    print("Filter list : ",list2)

    #map
    for no in list2:
        list3.append(no + 2)

    print("Map list : ",list3)

    #reduce
    sum=0
    for no in list3 :
        sum = sum + no

    print(sum)

if __name__=="__main__":
    main()