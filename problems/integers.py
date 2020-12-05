
'''Length of an integer'''
def length(n):
    if n==0: return 1
    if n<0:n=-n
    i=0
    while n:
        i+=1;n/=10
    return i

def reverse(n):
    sum=0;m=n;k=10**(length(n)-1)
    if n<0:n=-n
    while n:
        sum+=k*(n%10)
        n/=10;k/=10
    if m<0:
        return -sum
    return sum


#Swap two numbers without temp variable
def swap(a,b):
    a+=b;b=a-b;a=a-b
    return(a,b)


def swap_xor(a,b):
    a^=b;b^=a;a^=b
    return (a,b)

import random
from random import lognormvariate
def rand(min, max):
    n=random.uniform(0.0,1.0)
    print(n)
    return int(n*(max-min)+min)


def unique(list):
    list.sort();prev=None
    for val in list:
        if prev is not None and val != prev:
            yield val
        prev=val

def unique_stable(list):
    dupes=set()
    for val in list:
        if val not in dupes:
            dupes.add(val)
            yield val

#String rotation
def str_rot(s1,s2):
    return s2 in s1+s1



def remove(list, values_to_remove):
  new_length = len(list)
  for index, value in enumerate(list):
    if index >= new_length:
      continue
    if value in values_to_remove:
      list[index] = list[new_length - 1]
      new_length -= 1
  return list[:new_length]


def sum(n):
    s=0
    while n:
        s+=n%10;n/=10
    return s

def digits(n):
    while n:
        yield n%10
        n/=10


def last_digit(n):
  return n%10



#Driver Codef
if __name__ == "__main__":
    print(length(-34534))
    print(reverse(-221))
    print(swap(2,3))
    print(swap_xor(2,3))
    print([rand(0, 10) for _ in range(5)])
    print(list(unique([1,2,2,1,1,23,4])))
    print(list(unique_stable([4, 2, 1, 4, 1, 3, 5, 1])))
    print(str_rot('rispete', 'peteris'))
    print(remove([1, 2, 3, 4, 5, 6, 7, 8], [2, 3]))
    print(list(digits(123)))
    print(last_digit(123))