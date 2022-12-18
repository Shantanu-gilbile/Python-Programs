class Arithematic:
    def __init__(self,A,B):
        print("Inside Init Method")
        self.no1 = A
        self.no2 = B

    def addition(self):
        ans = self.no1 + self.no2
        return ans

    def substraction(self):
        ans = self.no1 - self.no2
        return ans


def main():
    print("Inside main method")
    obj = Arithematic(11,10)

    output = obj.addition()
    print("Addition is : ",output)

    output = obj.substraction()
    print("Addition is : ", output)

if __name__=="__main__":
    print("Inside Starter")
    main()