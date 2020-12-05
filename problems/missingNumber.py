'''Missing Value/Number'''

#Summation/Formula Method
def missingNumber(arr):
    sum1=0
    total=arr[-1]*(arr[-1]+1)//2
    sum1=sum(arr)
    return total-sum1

#XOR Method
def missingNumber1(arr):
    l=len(arr)
    xor=arr[0]
    for i in range(1,l):
        xor=xor^arr[i]
    xor1=0
    for i in range(1,l+2):
        xor1=xor1^i
    return xor^xor1

#Driver'd Code
if __name__ == "__main__":
    print(missingNumber([1,2,4,5,6,7]))
    print(missingNumber1([1,2,4,5,6,7]))