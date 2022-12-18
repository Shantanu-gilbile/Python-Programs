#accept 2 numbers and perform addition and substraction

#class = characteristic + behaviour
#class= data + function

class Arithematic:
    def __init__(self,a,b):
        self.no1=a
        self.no2=b

    def add(self):
        return self.no1 + self.no2

    def sub(self):
        return self.no1 - self.no2


def main():
    print("Enter first number : ")
    value1=int(input())

    print("Enter Second number : ")
    value2= int(input())

    obj=Arithematic(value1,value2)

    ans = obj.add()
    print("Addition is : ",ans)

    ans = obj.sub()
    print("Substraction is : ", ans)

if __name__=="__main__":
    main()