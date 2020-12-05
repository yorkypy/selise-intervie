'''Python | Frequency of each character in String'''

def solve(s):
    dict={}
    for i in s: 
        if i in dict: 
            dict[i]+=1
        else: 
            dict[i]=1
    return dict



def solve1(s):
    from collections import Counter 
    return Counter(s)

#Using dict.get()
'''
   get() method is used to check the previously occurring 
   character in string, if its new, it assigns 0 as initial 
   and appends 1 to it, else appends 1 to previously holded 
   value of that element in dictionary. 
'''
def solve2(s):
    res = {} 
    for key in s: 
        res[key]=res.get(key,0)+1
    return res


#Driver Code
if __name__ == "__main__":
    print(solve('GeeksforGeeks'))
    print(solve1('GeeksforGeeks'))
    print(solve2('GeeksforGeeks'))