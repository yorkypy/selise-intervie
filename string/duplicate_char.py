'''How do you print templicate characters from a string?'''

def solve(s):
    temp=[];dup=set()
    for i in range(len(s)):
        if s[i] not in temp:
            temp.append(s[i])k
        else:
            dup.add(s[i])
    return dup


#Driver Code
if __name__ == "__main__":
    print(solve('nimainnin'))
