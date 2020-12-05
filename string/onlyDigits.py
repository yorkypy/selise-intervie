'''How do you check if a string contains only digits?'''

def solve(s):
    try:
        if int(s):
            return True
    except:
        return False

def solve1(s):
    for i in range(len(s)):
        if s[i] == '0' and s[i] <= '9':
            return True
    return False


#Driver Code
if __name__ == "__main__":
    print(solve('233n'))
    print(solve1('233n'))