def demo():
    print("Inside demo")

def fun():
    print("Inside fun")

def hello(FPTR):
    print("Inside hello")
    FPTR()

hello(demo)
hello(fun)

