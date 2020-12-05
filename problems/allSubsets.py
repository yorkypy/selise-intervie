def allSubsets(arr):
    subset=[]
    subset(arr,subset,0)

def helper(arr,subset,i):
    if i==len(arr):
        print(subset)
    else:
        subset[i]=None
        helper(arr,subset,i+1)
        subset[i]=arr[i]
        helper(arr,subset,i+1)


    

if __name__ == "__main__":
    print(allSubsets({1,2,4,5}))

