#Solution I
class Solution:
    def minNum(self, arr, n):
        temp=sum(arr)
        if temp&1 != 1:
            return 2
        return 1

#Solution II
def minSum(arr):
    sum=0 
    for i in range(len(arr)):
        sum+=arr[i]
    if (sum%2) == 0:
        return 2
    return 1

if __name__ == "__main__":
    print(Solution().minNum([2,12,2,9],3))
    print(minSum([3896, 7464, 4710, 6113, 6108, 5592, 321, 7848, 2360, 1008, 3549, 7791, 2394, 3880, 5313, 2576, 6596, 7093, 1208, 9673, 968, 8215, 7890, 4781, 4989]))

