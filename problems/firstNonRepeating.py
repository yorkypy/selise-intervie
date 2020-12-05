'''First Non-repeating Character'''


#Solution I: O(n2)
def firstNonRepeating(s):
    for i in range(len(s)):
        seenDuplicate=False
        for j in range(len(s)):
            if s[i]==s[j] and i!=j:
                seenDuplicate=True
                break
        if not seenDuplicate:
            return s[i]
    return '_'

#Solution II
def firstNonRepeating1(s):
    dict={}
    for i in range(len(s)):
        key=s[i]
        if key not in dict:
            dict[key]=1
        else:
            dict[key]+=1
    for key,value in dict.items():
        if value==1:
            return key

#Solution III
def firstNonRepeating2(s):
    dict={}
    for i in range(len(s)):
        key=s[i]
        if key not in dict:
            dict[key]=1
        else:
            dict[key]+=1
    counter=0
    for i in range(len(s)):
        if dict[s[i]]==1:
            return s[i],counter
        counter+=1

#Solution IV
def firstNonRepeating3(s):
    for i in range(len(s)):
        if s.index(s[i])==s.rindex(s[i]):
            return s[i]
    return '_'

#Driver Code
if __name__ == "__main__":
    print(firstNonRepeating('nimadsjdbsdvbvsdsnim'))
    print(firstNonRepeating1('nimadsjdbsdvbvsdsnim'))
    print(firstNonRepeating2('nimadsjdbsdvbvsdsnim'))
    print(firstNonRepeating3('nimadsjdbsdvbvsdsnim'))
