'''Python | Count and display vowels in a string'''
 
def solve(s,v):
    return [i for i in s if i in v] 
    


#Driver
if __name__ == "__main__":
    v=['A','a','E', 'e','I','i','O','o','U','u']
    print(solve('Nima isnnsdn ds aeio',v))
    