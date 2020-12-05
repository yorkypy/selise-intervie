'''Ways to remove i’th character from string in Python'''

#Naive Solution
def solve(s,n):
    s1=''
    for i in range(len(s)):
        if i != n:
            s1+=s[i]
    return s1

#While loop
def solve1(s,n):
    s1='';i=0
    while i<len(s):
        if i != n:
            s1+=s[i]
        i+=1
    return s1

#Using replace()

def solve2(s,i):
    return s.replace(s[i],'')



#Using slicing API
def solve3(s,n):
    return s[:n]+s[n+1:]
    

#Driver Code
if __name__ == "__main__":
    print(solve('nimayon',3))
    print(solve1('nimayon',3))
    print(solve2('nimayon',3))
    print(solve3('nimayon',3))


