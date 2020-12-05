'''Sort Color'''

def sortColor(arr):
    size=len(arr)
    red=0
    blue=0
    for i in range(size):
        if arr[i]==1:
            red+=1
        elif arr[i]==2:
            blue+=1
    return [1]*red + [2]*blue + [3]*(size-red-blue)


#Driver Code
if __name__ == "__main__":
    print(sortColor([1,2,4,1,3,2,1,2,3,1]))