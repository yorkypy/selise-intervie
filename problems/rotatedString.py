'''Rotated Strings'''

def rotatedStrings(str1):
    size=len(str1)
    temp=str1+str1
    for i in range(size):
        for j in range(size):
            print(temp[i+j],end='')
        print()

def checkSubstring(str1,str2):
    if len(str1) != len(str2):
        return False
    temp=str1+str1
    if str2 in temp:
        return True


#Driver Code
if __name__ == "__main__":
    print(rotatedStrings('nima'))
    print(checkSubstring('anu','nua'))