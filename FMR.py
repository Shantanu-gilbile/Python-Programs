
def CheckEven(no):
    return (no % 2==0)

def doubles(no):
    return no*2

def sum(a,b):
    return a+b

def filterX(helper_function, data):
    result = []
    for no in data:
        if(helper_function(no) == True):
            result.append(no)
    return result

def mapx(helper_function,data):
    result=[]
    for no in data:
        value = helper_function(no)
        result.append(value)
    return result

def reducex(helper_function, data):
    ans=0
    for no in data:
        ans=helper_function(ans,no)

    return ans



def main():
    iSize=int(input("Enter the Number of Element you want to store in list  :"))

    Data_input = list()
    for i in range(0,iSize,1):
        value=int(input(f"Enter the Number at {i} th location  :"))
        Data_input.append(value)

    print("Data is : ",Data_input)

    Data_filter=filterX(CheckEven, Data_input)

    print("Data after filter is : ",Data_filter)

    Data_map=mapx(doubles,Data_filter)

    print("Data after map is : ",Data_map)

    output = reducex(sum,Data_map)

    print("Result after reduce is : ",output)

if __name__=="__main__":
    main()