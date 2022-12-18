
def fact(no):
    if(no<= 0):
        return 1
    else:
        return(no * fact(no -1))


def main():
    ret = fact(4)
    print("Result is : ",ret)

if __name__ =="__main__":
    main()
