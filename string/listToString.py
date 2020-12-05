'''Python ode onvert ist of trings to a single sentence'''

#Solution I
def solve(arr):
    sen=''
    for i in range(len(arr)):
        sen=sen + ' ' + arr[i]
    return sen.strip()

#Solution II
def solve1(arr):
    return ' '.join(arr)

#Solution III
def solve2(arr):
    return ' '.join([i for i in arr])


if __name__ == "__main__":
    print(solve(['I', 'want', 'to', 'learn', 'Python']))
    print(solve1(['I', 'want', 'to', 'learn', 'Python']))
    print(solve2(['I', 'want', 'to', 'learn', 'Python']))
