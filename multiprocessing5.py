import time
import multiprocessing

def displayeven(no):
    for i in range(1,no):
        if (i % 2 == 0):
            print("Even number : ",i)

def displayodd(no):
    for i in range(1,no):
        if (i % 2 != 0):
            print("Odd number : ",i)


def main():
    print("Demonstration of a Parallel programming using multiple processor.")
    number = 200
    p1 = multiprocessing.Process(target = displayeven, args=(number,))
    p2 = multiprocessing.Process(target = displayodd, args=(number,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("End of main")

if __name__ == "__main__":
    start_time = time.process_time()
    main()
    end_time = time.process_time()
    print("Executiuon time is : ",end_time - start_time)