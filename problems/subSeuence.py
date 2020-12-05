def subSequence(str1):
    for i in range(len(str1)):
        for j in range(i,len(str1)):
            print(str1[i:j+1], end=' ')
        print(end='')
print(subSequence('net'))