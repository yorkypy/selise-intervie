def anagram(str1,str2):
    if sorted(str1)==sorted(str2):
        return 'Anagram'
    else:
        return 'Not Anagram'


def anagram1(str1):
    if str1==None:
        return -1
    dict={}
    for i in range(len(str1)):
        word=''.join(sorted(str1[i]))
        if word not in dict:
            dict[word]=i+1
        else:
            dict[word]=(i+1)
    return dict


#Driver Code
if __name__ == "__main__":
    print(anagram('nima','inddma')) 
    print(anagram1(['cta','cat','atc','nima']))

