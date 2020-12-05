
#Brute Force
def sumOfTwo(arr1,arr2,value):
    for i in range(len(arr1)-1):
        t_value=value-arr1[i]
        for j in range(len(arr2)-1):
            if arr2[j]==t_value:
                return True
    return False


#Optimal Solution
def sumOfTwo1(arr1,arr2,value):
    temp=[]
    for i in range(len(arr1)-1):
        temp.append(value-arr1[i])
    for j in range(len(arr2)-1):
        if arr2[j] in temp:
            return True
    return False

#Driver Code
arr=[]
for k in range(10000):
    arr.append(k)

if __name__ == "__main__":
    print(sumOfTwo(arr,arr,10000))
    print(sumOfTwo1(arr,arr,10000))

    #print(sumOfTwo1([2,-2,4,2],[2,-33,2,3],-35))
