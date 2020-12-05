'''First Duplicate: Elements must be in rane of the length of the array'''


#Solution I: Brute Force 
def firstDuplicate(arr):
    size=len(arr)
    minIndex=size
    for i in range(size):
        for j in range(i+1,size):
            if arr[i]==arr[j]:
                minIndex=min(minIndex,j)
    if minIndex==size:  
        return -1
    else:
        return arr[minIndex]



#Solution II
def firstDuplicate1(arr):
    seen=set()
    for i in range(len(arr)):
        if arr[i] in seen:
            return arr[i]
        else:
            seen.add(arr[i])
    return -1
    
#Solition III
def firstDuplicate2(arr):
    for i in range(len(arr)):
        if arr[abs(arr[i])-1]<0:
            return abs(arr[i])
        else:
            arr[abs(arr[i]-1)]=-arr[abs(arr[i]-1)]
    return -1


#Driver Code
if __name__ == "__main__":
    print(firstDuplicate([2,2,3,5,3,2]))
    print(firstDuplicate1([2,1,3,5,3,2]))
    print(firstDuplicate2([2,1,3,5,3,2]))

