from innimport import subdtraction

def decorated_function(function_name):
    def inner(a,b):
        if(a < b):
            a,b = b,a
        return function_name(a,b)
    return inner

def main():
    value1 = int(input("Enter first Number : "))
    value2 = int(input("Enter Second Number : "))

    new_function = decorated_function(subdtraction)
    print(new_function(value1,value2))

if __name__ =="__main__":
    main()
