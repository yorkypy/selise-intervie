'''Count Words in a String'''

def solve(s):
    import string
    count=0
    temp=''
    for i in range(len(s)):
        if s[i] != ' ' and s[i] != string.punctuation:
            temp+=s[i]     
        else:
            count+=1
            temp=''
    return count


def solve1(s):
    import re 
    return len(re.findall(r'\w+', s)) 


if __name__ == "__main__":
    print(solve('Geeksforgeeks, is best @# @Compu@ter Science Portal.!!!'))
    print(solve1('Geeksforgeeks, is best @# @Computer Science Portal.!!!'))
    