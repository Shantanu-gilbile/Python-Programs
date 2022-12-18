
def add(no):
    ans = 0
    while(no >= 0):
        ans = ans + no
        no = no -1
    return ans

def main():
    ret = add(4)
    print("Result is : ",ret)

if __name__ =="__main__":
    main()
