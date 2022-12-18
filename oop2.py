class addlist:

    def __init__(self):
        self.list1 = list()
        self.size = 0

    def accept(self):
        self.size = int(input("Enter the Number of values in List : "))

    def lista(self):
        for i in range(self.size):
            no2  = int(input("Enter the numbers : "))
            self.list1.append(no2)

    def display(self):
        print(self.list1)

    def addlis(self):
        sum = 0
        for i in self.list1:
            sum = sum + i
        return sum

def main():
    obj = addlist()
    obj.accept()
    obj.lista()
    obj.display()
    addList = obj.addlis()
    print("Addition of Element in List are : ", addList)


if __name__=="__main__":
    main()