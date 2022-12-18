"""
def facter(value1):
    A=list()

    i=1
    while(i<int(value1/2)+1):
        if (value1 % i ==0):
            A.append(i)
        i+=1
    return A

    for i in range(1,(value1//2)+1):
        if (value1 % i == 0):
            A.append(i)
    return A

   """
#import sepfile
#from sepfile import *
from sepfile import facter


def main():
    no=int(input("Enter the number : "))

    ans=facter(no)

    print(f"Factors of {no} are : ",ans)

if __name__=="__main__":
    main()
