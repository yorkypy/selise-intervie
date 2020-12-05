def add(arr):
    return arr[0] if len(arr)==1 else arr[0]+add(arr[1:])
    
def fact(n):
    return 1 if n==0 or n==1 else n*fact(n-1)
 
def rev(l):
    return [l[-1]]+rev(l[:-1]) if l else []



#Driver Code
if __name__ == "__main__":
    print(add([1,2,1,3,1,3,2,3]))
    print(fact(10))
    print(rev([2,4,5,2,7]))
