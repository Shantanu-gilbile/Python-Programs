#variable number argument
def add(*values):
    print(type(values))
    print("Number of arguments are : ",len(values))

    sum = 0

    for no in values:
        sum = sum + no

    return sum

def main():
    ans =add(1,7,9,4,6,5)
    print("Addition is : ",ans)

if __name__=="__main__":
    main()


