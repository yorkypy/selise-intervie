#Solution I
def minValToBalance(arr):
    l=int(len(arr)/2)
    L=sum(arr[:l])
    R=sum(arr[l:])
    if L>R:
        n=L-R
    else:
        n=R-L
    return n    


#Solution II
def minValToBalance1(arr):
    sum1=0
    sum2=0
    for i in range(0,int(len(arr)/2)):
        sum1+=arr[i]
    for j in range(int(len(arr)/2), len(arr)):
        sum2+=arr[j]
    if sum1>sum2:
        num=sum1-sum2
    else:
        num=sum2-sum1
    return num

if __name__ == '__main__':
    lists=[12,1,21,21]
    print(minValToBalance(lists))
    print(minValToBalance1(lists))
    
