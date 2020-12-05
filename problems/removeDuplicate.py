'''Remove Duplicate From a Sorted Array'''

def solve(arr):
    n=len(arr);p=0;temp=[0]*n
    if n==0 or n==1:
        return arr
    for i in range(n-1):
        if arr[i] != arr[i+1]:
            temp[p]=arr[i]
            p+=1
    temp[p]=arr[n-1]
    return temp[0:p+1]


def solve1(arr):
    n=len(arr);p=0
    if n==0 or n==1:
        return arr
    for i in range(n-1):
        if arr[i] != arr[i+1]:
            arr[p]=arr[i]
            p+=1
    arr[p]=arr[n-1]
    return arr[0:p+1]

[1,2,3,3,3,4,5,6,7]
temp=[1,2,3,4,5,6,7]


#Driver Code
if __name__ == "__main__":
    print(solve([1,2,3,4,4,5,5,5,5,5,5,10,0]))
    print(solve1([1,2,3,4,4,5,5,5,5,5,5,10,0]))


