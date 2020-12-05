'''Python | Remove empty strings from list of strings'''


def solve(s):
    return [i for i in s if i] 


def solve1(s):
    while('' in s) : 
        s.remove('') 


def compress(chars):
        dict={};temp='';c=1
        for i in range(len(chars)):
            if chars[i] not in dict:
                dict[chars[i]]=c
            else:
                dict[chars[i]]+=c
        for k,v in dict.items():
            if v==1: 
                temp+=str(k)
            else:
                temp+=str(k)+str(v)
        return temp


#Driver Code
if __name__ == "__main__":
    print(solve(['sknsd','','vsd']))
    print(solve(['sknsd','','vsd']))
    print(compress(['a','a','m','s','s']))