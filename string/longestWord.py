'''Longest Word In A Sentence'''

#Using Python API
def solve(str1):
    return max(str1.split(), key=len)


#Using for loop
def solve1(str1):
    temp='';longestWord=0
    word=[]
    for i in range(len(str1)):
        if str1[i] != ' ':
            temp+=str1[i]
        else:
            longestWord=max(longestWord,len(temp))
            word.append(temp)
            temp=''
    word.append(temp) #For the last word
    return max(longestWord,len(temp)), max(word,key=len)


#Driver Code
if __name__ == "__main__":
    print(solve('nima ani asnain bdidsbvisdkbvsdi'))
    print(solve1('nima ani asnain bdidsbvisdkbvsdi'))
