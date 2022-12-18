class value:

    def __init__(self,data):
        self.no=data

    def sumfactor(self):
        sum = 0

        for i in range(1,(self.no // 2) +1):
            if(self.no % i == 0):
                sum = sum + i

        return sum

    def checkperfect(self):
        ans = self.sumfactor()

        if(self.no == ans):
            return True
        else:
            return False

    def prime(self):
        flag = True
        for i in range(2,(self.no//2) + 1):
            if (self.no % i == 0):
                flag = False
                break
        return flag




        """   
        if self.no ==2:
            return True

        else:
            for i in range(2,(self.no //2)+1):
                if (self.no % 2 == 0):
                    return False
                else:
                    return True
        """

def main():
    a = int(input("Enter the number : "))

    obj = value(a)

    print("Sum of Factor is : ",obj.sumfactor())

    ret = obj.checkperfect()
    if ret == True:
        print(f"{a} is Perfect number")

    else:
        print(f"{a} is Not a Perfect number")

    ret = obj.prime()

    if ret == True:
        print(f"{a} is Prime Number")

    else:
        print(f"{a} is Not Prime")

if __name__=="__main__":
    main()