def convertToWave(A):
    for i in range(0,len(A)-1,2):
        if A[i]<A[i+1]:
            A[i],A[i+1]=A[i+1],A[i]
    return A
print(convertToWave([1,2,4,3,6,3,42,2,2]))
