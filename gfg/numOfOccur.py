def numOfOccur(arr,x):
    count=0
    for i in range(len(arr)):
        if x==arr[i]:
            count+=1
    return count
    
if __name__ == '__main__':
    print(numOfOccur([2,2,1,2,12,12,12],12))
