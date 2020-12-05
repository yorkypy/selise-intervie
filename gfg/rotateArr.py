def rotateArr(arr,s):
    l=arr[:s]
    r=arr[s:]
    return r+l


def rotateArr1(arr,s):
    rotated=[]
    for i in range(s,len(arr)):
        rotated.append(list(arr[i]))
    for j in range(0,s):
        rotated.append(list(arr[j]))
    return rotated

   
if __name__ == "__main__":
    print(rotateArr([1,2,4,3,42],3))
    print(rotateArr([1,2,4,3,42],3))