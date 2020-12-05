import random
def shuffleArr(arr):
    new_arr=[]
    for i in range(len(arr)-1):
        new_arr.append(random(i))
    return new_arr


if __name__ == "__main__":
    print(shuffleArr([2,3,1,3,33,2,3,3]))