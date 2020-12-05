names=['Nima','Yonten','Pema','John Doe']

def sortBySecondChar(str):
    return sorted(str, key=lambda k:k[1])
print(sortBySecondChar(names))

def sortBySecondChar1(str):
    for i in range(len(str)-1):
        for j in range(i+1,len(str)):
            if ord(str[i][1])>ord(str[j][1]):
                str[i],str[j]=str[j],str[i]
    return str
print(sortBySecondChar1(names))
