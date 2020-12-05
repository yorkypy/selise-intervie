#Binary Search

from typing import Sized


def binarySearch(arr,n):
    size=len(arr)
    for i in range(size):
        if arr[(size/2)]==arr[i]:
            return arr[i]
        elif n>arr[(size/2)]:
            pass

if __name__ == "__main__":
    pass

