
#Square
print([i**2 for i in range(10) if i>3])

#Odd/Even
print([i for i in range(10) if i%2!=0])
print([i for i in range(10) if i%2==0])

#Multples of 10
print([i*10 for i in range(10)])

#Printing all numbers from a string
s='Nima is 24 years old and w33k5'
print(''.join([i for i in s if i.isnumeric()]))

#Printing an index
ages=[2,2,3,2,3,2,3,3,23,2]
print([a for a,i in enumerate(ages) if i==23])

#Delete
import random
letters=[i for i in 'NJNSKNKSNNDS']
random.shuffle(letters)
print([l for l in letters if l != 'S'])

#If-else
nums=[23,2,3,2,3,232,23,2,24,34]
print(str([i if i%2==0 else i*10 for i in nums]))

#nested loop iteration
a=[[2,3,2,3],[3,3,2,3]]
print([x for b in a for x in b])