'''Python | Check if a variable is string'''


def isString(s):
    return type(s)

def isString1(s):
    return isinstance(s,str)

#Driver Code
if __name__ == "__main__":
    print(isString('sdsndv'))
    print(isString1('sdsndv'))