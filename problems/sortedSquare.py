def sortedSquare(lis):
    sq_lis=[]
    for n in range(len(lis)):
        sq_lis.append(lis[n]*lis[n])        
    return sorted(sq_lis)

def sortSqr(arr):
    l=0
    r=len(arr)-1
    res=[]
    for i in range(len(arr),-1,-1):
        if abs(arr[l])>abs(arr[r]):
            res.append(arr[l]*arr[l])
            l+=1
        else:
            res.append(arr[r]*arr[r])
            l-=1
    return res

#Driver Code
if __name__ == "__main__":
    print(sortedSquare([-4,3,-2,-442,35,4,-2,200]))
    print(sortSqr([-4,3,-2,-442,35,4,-2,200]))


