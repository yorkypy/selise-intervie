'''Python | Test if string contains element from list'''


def solve(arr,s):
    return any(i in s for i in arr)



#Drive Code
if __name__ == "__main__":
    print(solve(['ksd','nima','anv'],'Nima is a coder'.casefold()))
