matrix=[
            [1,2,3,4],
            [5,6,7,8],
            [9,10,11,12]
    ]
print([[row[i] for row in matrix] for i in range(4)])
final_list=[]
for i in range(4):
    lis=[]
    for row in matrix:
        lis.append(row[i])
    final_list.append(lis)
