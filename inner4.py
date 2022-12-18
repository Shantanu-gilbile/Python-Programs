
def outer():
    print("Inside outer")

    def inner():
        print("Inside inner")

    print(id(inner))

    return inner

ret = outer()
print(type(ret))
print(id(ret))
ret()

