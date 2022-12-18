def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def calculator(Target,value1,value2):
    return Target(value1,value2)

ret = calculator(add,10,11)
print("Addition is : ",ret)

ret = calculator(Target = sub,value1=10,value2=11)
print("Substraction is : ",ret)