import os
import multiprocessing

def square(no):
    print(f"PID of worker process is {os.getpid()} for the input {no}")
    return no * no

def main():
    print("Process ID of our application is : ",os.getpid())

    data = [1,2,3,4,5]

    pool = multiprocessing.Pool()

    result = pool.map(square,data)

    print("Result after square operation is : ",result)

if __name__ == "__main__":
    main()