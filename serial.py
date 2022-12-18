def square(no):
    return no * no

def main():

    data = [1,2,3,4,5]
    result = []

    for value in data:
        result.append(square(value))

    print("Result after square operation is : ",result)

if __name__ == "__main__":
    main()