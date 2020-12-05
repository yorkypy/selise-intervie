#A simple sorting program that returns second highest number
def secondHighest(lis):
    if len(lis)==1 or len(lis)==None:
        return None
    for i in range(len(lis)-1):
        for j in range(i+1, len(lis)):
            if lis[i]>=lis[j]:
                temp = lis[i]
                lis[i] = lis[j]
                lis[j] = temp 
    return lis[-2]

def secondHighest1(arr):
    highest=None
    secondHighest=None
    for i in arr:
        if highest==None:
            highest=i
        elif i>highest:
            secondHighest=highest
            highest=i
        elif secondHighest==None:
            secondHighest=i
        elif i>secondHighest:
            secondHighest=i
    return secondHighest


#Driver Code
if __name__ == "__main__":
    lis=[2]
    print(secondHighest(lis))
    print(secondHighest1(lis))

