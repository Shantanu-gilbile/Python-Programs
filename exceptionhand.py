def main():
    no1 = int(input("Enter the number 1 : "))

    no2  = int(input("Enter the number 2 : "))

    try :
        ans = no1 /no2
        print("Division is : ",ans)

    except ZeroDivisionError:
        print("HHH")

    except Exception:
        print("Inside last except block")

    finally :
        print("Inside last except block")
if __name__ =="__main__":
    main()