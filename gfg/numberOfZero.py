#1's on left and 0's on right

def countZeroes(arr):
    count=0
    for i in range(len(arr)-1,-1,-1):
        if arr[i] == 0:
            count+=1
        else:
            break
    return count

if __name__ == "__main__":
    print(countZeroes([1,1,1,1,1,1,0,0,0,0]))                