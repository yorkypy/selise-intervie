def isPrime(num):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                return 'Not Prime'
        return 'Prime'

#Driver Code
if __name__ == "__main__":
    print(isPrime(10000019))
