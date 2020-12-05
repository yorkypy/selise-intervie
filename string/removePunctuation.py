'''Python | Remove punctuation from string'''


def solve(s):
    import string
    for i in s:
        if i in string.punctuation:    
            s=s.replace(i,'')
    return s


#Driver Code
if __name__ == "__main__":
    print(solve('ni@nksd {]][@#'))

