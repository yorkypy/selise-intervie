'''Min Subsets with Consecutive Numbers '''


def solve(arr):
    arr=sorted(arr)
    count=1
    for i in range(len(arr)-1):
        if arr[i]+1 != arr[i+1]:
            count+=1
    return count

def solve(arr):
    win=[];l=0
    for i in range(len(arr)):
        if arr[i+1]-arr[i] == 1:
            win.append(arr[i])
            l+=1








#Driver Code
if __name__ == "__main__":
    print(solve([23,45,22,1,21,44,20,3,2]))
    