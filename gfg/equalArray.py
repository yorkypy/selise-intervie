#using Python API
def equalArr(arr1,arr2):
    if len(arr1) != len(arr2):
        return False
    elif sorted(arr1)==sorted(arr2):
        return True
    return False


if __name__ == '__main__':
    list1=[1,2,1,2]
    list2=[2,1,1,2]
    print(equalArr(list1,list2))

