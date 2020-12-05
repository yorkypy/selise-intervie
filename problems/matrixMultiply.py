m1=[
    [1,2,1],
    [1,3,2],
    [32,2,1]
]
m2=[
    [3,32,3],
    [3,2,3],
    [3,0,3]
]

for i in range(len(m1)):
    for j in range(len(m2)):
        print(m1[i][0]*m2[j][0])


