'''Python | Extract numbers from string'''

#Not Working
def solve(s):
    num=[];temp=''
    for i in range(len(s)):
        if s[i].isdigit():
            temp+=s[i] 
    num.append(temp)
    return num

    
def solve1(s):
    return [int(i) for i in s.split() if i.isdigit()]


if __name__ == "__main__":
    print(solve('Nima is 24 years 23 and w'))
    print(solve1('Nima is 24 years and w23'))

