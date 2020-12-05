def solve(s):
    import string
    if string.punctuation in s:
        s=s.replace(string.punctuation,'')
    l=s.split()
    l1=0
    for i in range(len(l)):
        l1+=len(l[i])
    return l1/len(l)
        

#Driver Code
if __name__ == "__main__":
    print(solve('nimnd sknd nim'))