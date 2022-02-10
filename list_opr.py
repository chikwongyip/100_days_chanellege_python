list = [1,3,5,7,100]
list.append(100)
print(list)
list.insert(10,2000)
print(list)
for index,elem in enumerate(list):
    print(index,elem,end=' ')

# 如果元素在list 中可以操作
if 3 in list:
    list.remove(3)
    print(list,end=' ')
# 删除list 指定位置
print('\n')
list.pop(0)
print(list)