def displayeven(no):
    for i in range(1,no):
        if (i % 2 == 0):
            print("Even number : ",i)

def displayodd(no):
    for i in range(1,no):
        if (i % 2 != 0):
            print("Odd number : ",i)


def main():
        print("Demonstration of a serial programming")
        displayeven(2000)
        displayodd(2000)


if __name__ == "__main__":
    main()