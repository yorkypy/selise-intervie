def solve(n, s, lst):
    lst.append(0)
    starting = 0; 
    ending = 0; 
    cur_sum = lst[0]
    while starting < n and ending < n:
        if cur_sum == s:
            return "{:} {:}".format(starting+1, ending+1)
        elif cur_sum < s:
            ending += 1
            cur_sum += lst[ending]
        elif cur_sum > s:
            cur_sum -= lst[starting]
            starting += 1
    return -1
    

for _ in range( int(input()) ):
    n, s = list(map(int, input().strip().split(" ")))
    lst = list(map(int, input().strip().split(" ")))
    print(solve(n, s, lst))