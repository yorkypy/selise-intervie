def reverseInteger(x):
    r=''
    y=str(abs(x))
    for i in range(len(y)-1,-1,-1):
        r+=y[i]
    if x<0:
        return int(r)*-1
    return int(r)

#Driver Code
if __name__ == "__main__":
    print(reverseInteger(4324534200)) #int() automatically removes zero's