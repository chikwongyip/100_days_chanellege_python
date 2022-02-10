list = [1,2,3,4,5]
print(list)
list2 = ['hello','world',1]
print(len(list))
print(len(list2[0]))

#下标读list 元素
for index in range(len(list)):
     print(list[index],end= '\t')
#遍历lista 元素
for elem in list:
    print(elem,end='\n')

for index,elem in enumerate(list):
    print(index, elem,end='\n')