list_1=[8,5,8]
list_2=[5,2,5]
list_3=[(list_2[0]-list_1[0]),(list_2[1]-list_1[1]),(list_2[2]-list_1[2])]
print(list_3)

list_1=[8,5,8]
list_2=[5,2,5]
list_3=[]
for x in range (0,len(list_1)):
    b = list_2[x]-list_1[x]
    list_3.append(b)
print(list_3)
