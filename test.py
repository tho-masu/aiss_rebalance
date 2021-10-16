print(list(range(0,int(6.99)+1,1)))
array=[(1,2),(3,2),(2,1),(0,2)]
print(max(array,key=lambda element: (element[1],-element[0])))
list = list(range(30,61,0))
for element in list:
    print('execute')
l=[True,False,True,False,True]
print(l.count(False))