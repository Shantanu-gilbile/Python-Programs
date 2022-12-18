# positional argument / keyword argument
def add1(no1,no2):
    print("Value of no1 : ",no1)
    print("Value of no2 : ", no2)
    return no1 + no2

def sub1(no1,no2):
    print("Value of no1 : ",no1)
    print("Value of no2 : ", no2)
    return no1 - no2

def main():
    ans = add1(10,11)
    print("Addition is : ",ans)

    ans = sub1(no2=10, no1=11)
    print(" Substraction  is : ", ans)

    ans = sub1(no1=10, no2=11)
    print(" Substraction  is : ", ans)

if __name__=="__main__":
    main()