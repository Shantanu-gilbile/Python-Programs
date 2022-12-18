def facter(value1):
    A=list()

    i=1
    while(i<int(value1/2)+1):
        if (value1 % i ==0):
            A.append(i)
        i+=1
    return A