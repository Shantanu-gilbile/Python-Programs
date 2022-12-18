from addmod import add

def main():
    no1 = int(input("Enter the Value 1 : "))
    no2 = int(input("Enter the Value 2 : "))

    ans  = add(no1,no2)
    print(ans)
if __name__=="__main__":
    main()