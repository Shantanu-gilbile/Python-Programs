# Application to findout the maximum number

def maximum(value1,value2):
    if value1 > value2:
        return value1
    else:
        return value2

def main():

    no1 = int(input("Enter the First number : "))

    no2 = int(input("Enter the First number : "))

    ans=maximum(no1,no2)

    print("Largest number is : ",ans)

if __name__=="__main__":
    main()