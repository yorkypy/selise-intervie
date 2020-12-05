'''Minimum Difference'''

import sys
def minDifference(arr):
    size=len(arr)
    arr=sorted(arr)
    minDiff=sys.maxsize-1
    for i in range(size-1):
        if arr[i+1]-arr[i]<minDiff:
            minDiff=arr[i+1]-arr[i]
    return minDiff
            
#Driver Code
if __name__ == "__main__":
    print(minDifference([5,32,45,4,12,18,25]))
