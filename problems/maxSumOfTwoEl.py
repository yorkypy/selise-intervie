def maxSumOfTwoElement(arr):
    arr=sorted(arr)
    diff=-999*999
    for i in range(len(arr)-1):
        if arr[i+1]-arr[i]>diff:
            diff=arr[i+1]-arr[i]
    return diff
    
#Driver Code
if __name__ == "__main__":
    print(maxSumOfTwoElement([2,3,5,8,2,1,-4]))