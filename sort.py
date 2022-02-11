fruits = ['grape','apple','banana','strawberry','waxberry']
fruits += ['pineapple','watermelon']
# 切片复制操作
fruits_2 = fruits[1:4]
fruits_3 = fruits[:]
print(fruits)
print('\n')
print(fruits_2)
print('\n')
print(fruits_3)
# sorting
print('\n')
sort_fruits = sorted(fruits)
print(sort_fruits)
print('/n')
# sort by key word
len_sort_fruits = sorted(fruits,key=len)
print(len_sort_fruits)