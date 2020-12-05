'''Reverse characters of each word of a given string'''

def solve(s):
    temp=''
    ans=''
    for i in range(len(s)):
        if s[i] !=' ':
            temp+=s[i]
        else:
            temp=temp[::-1]      #reverse
            ans=ans + ' ' + temp
            temp=''
    ans=ans + ' ' + temp[::-1]
    return ans

def solve1(s):
    return ' '.join([i[::-1] for i in s.split()])

print(solve('this is as cat'))
print(solve1('this is as cat'))




