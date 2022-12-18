"""
class prime:
    def __init__(self,no1):
        self.no1=no1

    def prime1(self):
        if self.no1==2:
            return True
        else :
            for i in range(2,((self.no1)//2)+1):
                if self.no1 % i ==0:
                    return  False
                else :
                    True
def main():
    print("Enter first number : ")
    value1 = int(input())


    obj = prime(value1)

    ans = obj.prime1()

    if ans == True:
        print("Prime")

    else:
        print("Not Prime")


if __name__=="__main__":
main()


class factorial :
    def __init__(self,no1):
        self.no1=no1

    def fact1(self):
        fact = 1
        for i in range(1,self.no1 +1):
            fact = fact * i
        return fact

def main():
    value1 = int(input("Enter the name : "))

    obj = factorial(value1)
    ans  = obj.fact1()
    print(ans)

if  __name__=="__main__":
    main()

print("dd")
"""

def checkprime(lis):
    flag = True
    for i in range(2,(lis//2)+1):
        if lis % i == 0:
            flag = False
            break
    return flag

def prime(list1):
    A=[]
    for i in range(len(list1)):
        if(checkprime(list1[i]) == True):
            A.append(list1[i])

    return A




def main():
    list1 = [4,5,6,7,8,9]
    print(prime(list1))



if __name__ == "__main__":
    main()