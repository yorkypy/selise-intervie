'''How do you find all the permutations of a string?'''

#Recursive Solution
def permutate(s, step=0):
    if step == len(s):
        print(''.join(s))
    for i in range(step, len(s)):
        copy=[c for c in s]
        copy[step],copy[i]=copy[i],copy[step]
        permutate(copy,step+1)


#Usin built-in API
from itertools import permutations
def solve(s):
    return [''.join(p) for p in permutations(s)]

#Driver Code
if __name__ == "__main__":
    print(permutate('2332'))
    print(solve('sknsf'))


