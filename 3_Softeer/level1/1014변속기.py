asc=[1,2,3,4,5,6,7,8]
des=[8,7,6,5,4,3,2,1]
des=asc[::-1] # 원본리스트의 역순
des=list(reversed(asc)) #파이썬 내장함수 이용
# des=asc.reverse() => asc=[8,7,6,5,4,3,2,1] 로 바뀜.

lst=list(map(int,input().split()))

# if lst is asc  => X : is는 값이 같은지 보는게 아니라, 주소가 같은지 보는 것
if lst==asc:
    print("ascending")
elif lst==des:
    print("descending")
else:
    print("mixed")