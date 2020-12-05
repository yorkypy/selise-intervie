def freqOfChar(str1):
    freq=[]
    for i in range(len(str1)):
        for j in range(i,len(str1)):
            if i==j and i != j:
                freq.append(i)
            

