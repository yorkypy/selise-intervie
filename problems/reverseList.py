#Using reverse() API
list1=[34,4,4,6,2,4]
list1.reverse()
print(list1)

#Using Slicing
list2=[34,4,4,6,2,4]
print(list2[::-1])

#Using reversed() API: Doesn't modify original list
list3=[34,4,4,6,2,4]
print(list(reversed(list3)))

#Using for loop
list4=[34,4,4,6,2,4]
l=[]
for i in range(len(list4)-1,-1,-1):
    l.append(list4[i])
print(l)