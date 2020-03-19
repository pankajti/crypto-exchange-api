data =[23,23,12,98,34,36,9,22]


def quicksort(data,low,high):
    print(data)

    if low<high:
        pivot=partition(data,low,high)
        quicksort(data,low,pivot)
        quicksort(data,pivot+1,high)


def partition(data,low,high ):

    i=low-1
    j=high+1
    piot=data[low]
    while True:

        for count in range(high-low+1):
            i += 1
            if data[i]>=piot:
                break

        for count in range(high-low+1):
            j -= 1
            if data[j]<piot:
                break

        if i>=j:
            break
        else:
            temp=data[i]
            data[i]=data[j]
            data[j]=temp

            print("swapping {}  with {}".format(data[i],data[j]))
    return j









ret=quicksort(data,0,len(data)-1)
print(ret)
print(data)