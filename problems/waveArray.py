'''Wave Array: Even position elements are greater than that of odd ones'''

def waveArray(arr):
    size=len(arr)
    for i in range(0,size,2):
        if i>0 and arr[i-1]>arr[i]:
            arr[i-1],arr[i]=arr[i],arr[i-1]
        if i<size-1 and arr[i]<arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr

#Driver Code
if __name__ == "__main__":
    print(waveArray([3,2,6,7,5,12,10,9,8]))
