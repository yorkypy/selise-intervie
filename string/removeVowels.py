'''Remove Vowels'''

def solve(s):
    v=['a','e','i','o','u']
    new=''

    for i in range(len(s)):
        if s[i] not in v:
            new+=s[i]
    if new=='':
        return "''"
    return new

if __name__ == "__main__":
    print(solve('aeiouUUvdsfkdkdbdffo'.lower()))            

