#default parameter

def area(radius,pi = 3.14):
    result = pi * radius * radius
    return result

def main():
    rvalue = 10.5
    pivalue = 3.14

    #positinal argument
    ans =area(rvalue,pivalue)
    print("Atre of circle : ",ans)    # ans=area(10.5,3.14)

    #keyword argument
    ans = area(radius=rvalue,pi= pivalue)
    print("Area of circle : ", ans)

    # positinal argument and second is default
    ans = area(10.5)
    print("Area of circle : ",ans)

    #keyword argument and second is default
    ans = area(radius=10.5)
    print("Area of circle : ", ans)

    #keyword argument
    ans = area(pi = 7.10 ,radius=10.5)
    print("Area of circle : ", ans)


if __name__=="__main__":
    main()