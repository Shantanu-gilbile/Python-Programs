class addlist:

    def __init__(self):
        self.list1 = list()
        self.size = 0
        self.sum = 0
        self.accept()

    def accept(self):
        self.size = int(input("Enter the Number of values in List : "))

    def lista(self):
        for i in range(self.size):
            no2  = int(input("Enter the numbers : "))
            self.list1.append(no2)

    def display(self):
        print(self.list1)

    def maxele(self):
        max = self.list1[0]

        for i in self.list1:
            if i > max:
                max = i

        return max

    def minele(self):
        min = self.list1[0]

        for i in self.list1:
            if i < min:
                min = i

        return min

    def addlis(self):
        self.sum = 0
        for i in self.list1:
            self.sum = self.sum + i
        return self.sum

    def average(self):
        avg = self.sum / self.size
        return avg

    def __prime(self,no):
        flag = True
        for i in range(2,(no//2) + 1):
            if (no % i == 0):
                flag = False
                break
        return flag

    def checkprime(self):
        for i in range(0,self.size):
            if(self.__prime(self.list1[i])==True):
                print(f"{self.list1[i]}Prime number")

def main():

    obj = addlist()
    obj.lista()
    obj.display()

    maxx = obj.maxele()
    print("Maximum number from list is : ",maxx)

    minn = obj.minele()
    print("Maximum number from list is : ", minn)

    addList = obj.addlis()
    print("Addition of Element in List are : ", addList)

    avgg = obj.average()
    print("Average is : ",avgg)

    print(obj.checkprime())

if __name__=="__main__":
    main()