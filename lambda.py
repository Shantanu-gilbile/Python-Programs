#Normal functions / named function
"""
def add(no1,no2):
    return no1 + no2

#lamda function / unnamed function / ananomus function
# lamda parameters : body (syntax)

addfunction = lambda a,b : a+b

ans1=add(10,11)
ans2=addfunction(10,11)

print("Aaddition using normal function : ",ans1)
print("Addition using lamda function : ",ans2)

print("Type of lambda function is : ",type(addfunction))



def even(no1):
    if no1 % 2 == 0:
        return True
    else:
        return False


def checkevenx(no):
    return (no % 2 == 0)

ret = checkevenx(12)

if ret == True:
    print("Even")
else:
    print("Odd")

"""
even = lambda no1 : no1  % 2 == 0

ret = even(12)

if ret == True:
    print("Even")
else :
    print("Odd")

