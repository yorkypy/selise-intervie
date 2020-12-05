#Bubble Sort
def bubbleSort(arr):
    size=len(arr)
    sorted=False
    for i in range(size-1):
        for j in range(size-1-i):
            if arr[j]>=arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                sorted=True
        if not sorted:
            break
    return arr
    
#More Pythonic
def bubbleSort1(arr):
    size=len(arr)
    sorted=False
    for i in range(size-1):
        for j in range(len(arr)-1-i):
            if arr[j]>=arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                sorted=True
        if not sorted:
            break
    return arr

#Using while loop
def bubbleSort2(arr):
    sorted=False
    while not sorted:
        sorted=True
        for i in range(0,len(arr)-1):
            if arr[i]>arr[i+1]:
                sorted=False
                arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr

#Driver Code 
if __name__ == "__main__":
    print(bubbleSort([1,3,4,5,6])) 
    print(bubbleSort1(['za','xa','w','as']))
    print(bubbleSort2([1,3,-1,2,3,8,2]))
