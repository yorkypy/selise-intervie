#SELECTION SORT
def selectionSort(arr):
    for i in range(len(arr)-1):
        min=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min=j
        if min != i:
            arr[min],arr[i]=arr[i],arr[min]
    return arr

#Using while loop
def selectionSort1(arr):
    i=0
    while i<len(arr)-1:
        minIndex=i
        j=i+1
        while j<len(arr):
            if arr[j]<arr[i]:
                minIndex=j
            j+=1
        if minIndex != i:
            #swap(arr,minIndex,i)
            minIndex,i=i,minIndex
        i+=1

#Driver Code
if __name__ == "__main__":
    print(selectionSort([2,1,2,4,-21,3]))
    print(selectionSort1([2,1,2,4,-21,3]))




