'''Competitive Programming'''


def bear(a,b):
    ans=0
    while a<=b:
        a*=3;b*=2;ans+=1
    return ans

#Driver Code
if __name__ == "__main__":
    print(bear(1,9))