data =[23,23,12,98,34,36,9,22]

def bubblesort(data):
    for i in range(len(data)):
        for j in range(i+1,len(data)):
            if data[i]>data[j]:
                print("{} is greater than {} hence swapping".format(data[i],data[j]))
                temp=data[i]
                data[i]=data[j]
                data[j]=temp

bubblesort(data)
print(data)