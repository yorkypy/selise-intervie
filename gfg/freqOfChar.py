'''Freuency of Characters/Numbers'''

def freqSort(s):
    dict={}
    for i in range(len(s)):
        c=s[i];count=1
        if c not in dict:
            dict[c]=count
        else:
            dict[c]+=count
    for k,v in dict.items():
        print(f'{k} occurs {v} times')


def frequencycount(A,N):
    # code here
    dict={}
    for i in range(1,N+1):
        dict[i]=0
    l=[]
    for k,v in dict.items():
        for j in range(len(A)):
            if k==A[j]:            
                v+=1
        l.append(v)
        print(f"{k} occuring {v} times.")

def f(A,N):
    i=1;l=[];c=0
    while i<N+1:
        for j in range(len(A)):
            if N==A[j]:
                c+=1
        l.append(c)
        i+=1
    print(l)
f([1,1,1,1,1],5)

frequencycount([1,1,1,1,1],5)

#Driver Code
if __name__ == "__main__":
    freqSort('nalsniaidv')
    freqSort('00282438843*')
