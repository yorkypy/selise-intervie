def commonElement(l1,l2):
    common=set()
    count=0
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i]==l2[j] and l1[i] not in common:
                common.add(l1[i])
                count+=1
    return common,count


def commonChar(str1,str2):
    dict={}
    for i in str1:
        dict[i]=1
    common=set()
    for j in str2:
        if dict.get(j):
            common.add(j)
    return common
    
#Driver Code
if __name__ == "__main__":
    print(commonChar('vbdskndksndv','sdsnjjsbdvsvllsbf'))