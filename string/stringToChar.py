'''Python | Split string into list of characters'''


def solve(str1):
    l=[]
    for i in range(len(str1)):
        if str1[i] != ' ':
            l.append(str1[i])
    return l

#List Comprehension
def solve1(str1):
    
    return [i for i in str1]

#Type Casting
def solve2(word): 
    return list(word) 



#Driver Code
if __name__ == "__main__":
    print(solve('Nima is a coder'))
    print(solve1('Nima is a coder'))
    print(solve2('1234'))