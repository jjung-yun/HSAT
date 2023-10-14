print(dir([1,2]))

# 리스트
list1 = [1, 2, 3]
list2 = [4, 5, 6]

print(list1 + list2) # 출력: [1, 2, 3, 4, 5, 6]
print(list1 * 3)     # 출력: [1, 2 ,3 ,1 ,2 ,3 ,1 ,2 ,3]
print(2 in list1)    # 출력: True

#튜플
print(dir((1,2)))
t1 = (1, 2, 3)
t2 = (4, 5, 6)

print(t1 + t2)    # 출력: (1, 2, 3, 4, 5, 6)
print(t1 * 3)     # 출력: (1, 2 ,3 ,1 ,2 ,3 ,1 ,2 ,3)
print(2 in t1)    # 출력: True