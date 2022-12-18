
def display(no):
    if(no > 0):
        print("Hello world")
        no = no - 1
        display(no)  # Recursive functon call

def main():
    display(4)

if __name__ =="__main__":
    main()