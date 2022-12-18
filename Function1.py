#function which takes nothing and return nothing
def demo1():
    print("inside demo")

#function which takes one argument and return nothing
def demo2(no):
    print("Inside demo2 with argument : ",no)

#function which takes one argument and return one argument
def demo3(no):
    print("Inside demo3 with argument : ",no)
    return no + 2

#function which takes two argument  and return one argument
def demo4(no1,no2):
    print("Inside demo4")
    add = no1 + no2
    return add

#function which takes two argument  and return two argument(multiple)
def demo5(no1,no2):
    print("Inside demo5")
    add = no1 + no2
    sub= no1 - no2
    return add,sub

def main():
    demo1()

    demo2("Hello")

    ans = demo3(10)
    print("Return value of demo3 : ",ans)

    ans = demo4(10,11)
    print("Return value is  :",ans)

    ans1, ans2 = demo5(11, 10)
    print("Addition is : ",ans1)
    print("Substraction is : ",ans2)

if __name__=="__main__":
    main()
