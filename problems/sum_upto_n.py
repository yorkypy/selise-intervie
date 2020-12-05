
def add_it_up(n):
    sum=0
    try:
        for i in range(n+1):
            sum+=i
        print(sum)
    except TypeError:
        return 0
add_it_up(7)
