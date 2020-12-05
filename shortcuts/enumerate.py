
#Using normal range()
lis = [20,33,98,100,333,7767]
for i in range(len(lis)):
    num = lis[i]
    if num%2==0:
        lis[i]='ksnd'
print(lis)

#Using enumerate()
list = [20,33,98,100,333,7767]
for i, num in enumerate(list):
    if num%2==0:
        list[i]='ksnd'
print(list)

#List comprehension
print([num for num in enumerate([1,2,3])])
