def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def main():
    print("Enter first number : ")
    no1=int(input())

    print("Enter Second number : ")
    no2 = int(input())

    ans=add(no1,no2)
    print("Addition is : ",ans)

    ans = sub(no1, no2)
    print("Addition is : ", ans)


if __name__=="__main__":
    main()