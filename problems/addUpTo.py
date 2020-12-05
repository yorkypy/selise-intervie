def addUpTo(arr,n):
    size=len(arr);count=0
    for i in range(size):
        for j in range(i,size):
            if sum(arr[i:j+1])==n:
                count+=1
    return count

#Usin Sliding Window Alorithm



#Driver Code
if __name__ == "__main__":
    print(addUpTo([1,2,5,2,3,4],7))
