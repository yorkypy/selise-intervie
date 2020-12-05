'''
This code takes a list of numbers and returns a
new list with the last element incremented by one
'''
def newList(arr):
    num=''
    for i in range(len(arr[::-1])):
        num=str(arr[::-1][i])+num
    new_num=str(int(num)+1)
    new_ls = []
    for j in range(0, len(new_num)):
        new_ls.append(int(new_num[j]))
    return new_ls

print(newList([1,0,0,0,0,9]))

