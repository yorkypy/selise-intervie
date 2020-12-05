'''Longest Palindromic Substring'''

#Solution I: Brute Force
def solve(str):
    palin=[]
    for i in range(len(str)-1):
        for j in range(i+1,len(str)):
            if str[i:j]==str[i:j][::-1]:
                palin.append(str[i:j])
    return max(palin,key=len), len(max(palin,key=len))

def solve1(str):
    l=0;palin=''
    for i in range(len(str)):
        for j in range(i,len(str)):
            if str[i:j+1]==str[i:j+1][::-1]:
                if len(str[i:j])>l:
                    palin=str[i:j+1]+palin
                    l=len(str[i:j+1])
    return palin,l

#Recursive Solution
def solve2(X,s,e):
    if s>e:return 0
    if s==e:return 1
    if X[s]==X[e]:
        return solve2(X,s+1,e-1)+2
    return max(solve2(X,s,e-1),solve2(X,s+1,e))


#Driver Code
if __name__ == '__main__':
    print(solve('pythonisinohsimi'))
    print(solve1('pythonisinohsimi'))
    print(solve2('momh',0,len('momh')-1))





