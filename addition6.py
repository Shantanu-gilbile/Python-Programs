print("Application to demonstrate industrial programming")

import marvellousModule

def main():
    print("Value of __name__ from main is : ",__name__)
    print("Enter first number : ")
    no1 = int(input())
    print("Enter second number : ")
    no2 = int(input())

    sum = marvellousModule.addition(no1,no2)

    print("Addition is  : ",sum)

if __name__=="__main__":
    main()