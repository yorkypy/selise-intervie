#Brute Force Method: O(n2)
import sys
def maxSubArraySum(arr):
    size=len(arr)
    max_sum=-sys.maxsize-1
    for i in range(size):
        for j in range(i,size):
            current_sum=sum(arr[i:j+1])
            if current_sum>max_sum:
                max_sum=current_sum
    return max_sum


#Kandane's Algorithm: O(n)
def maxSubArraySum1(arr):
    cur_sum=0
    max_sum=arr[0]
    start=0;end=0;pointer=0
    for i in range(len(arr)):
        cur_sum+=arr[i]
        if max_sum<cur_sum:
           max_sum=cur_sum
           start=pointer
           end=i
        if cur_sum<0:
            cur_sum=0
            pointer=i+1
    return max_sum,start,end


def solve(arr):
    maxS=-999999*9999999
    for i in range(len(arr)-3):
        if arr[i]+arr[i+1]+arr[i+2]>maxS:
            maxS=arr[i]+arr[i+1]+arr[i+2]
    return maxS
print(solve([-1,-2,-1,-4,-1,-2,-1,-2,-1]))



#Driver Code
if __name__ == "__main__":
    print(maxSubArraySum([-2,2,-5,11,-6]))
    print(maxSubArraySum1([-2,2,5,11,-6]))

