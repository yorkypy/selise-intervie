
#Recursive Solution
def fact(n):
    return 1 if n==0 or n==1 else n*fact(n-1)

#Iterative Solution


#Driver Code
if __name__ == "__main__":
    print(fact(9))