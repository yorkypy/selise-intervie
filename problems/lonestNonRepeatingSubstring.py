'''Longest Non-repeating Substring'''

#Sliding Window Algorithm
def longestNonRepeatingSub(str1):
    if str1==None or len(str1)==0:
        return '_'
    i=j=maxL=0;temp=set()
    while i<len(str1):
        c=str1[i]
        while c in temp:
            temp.remove(str1[j])
            j+=1
        temp.add(c)
        maxL=max(maxL,i-j+1)
        i+=1
    return maxL

#Driver Code
if __name__ == "__main__":
    print(longestNonRepeatingSub(''))
    print(longestNonRepeatingSub('nia'))
    print(longestNonRepeatingSub('mkpjjh'))
        

