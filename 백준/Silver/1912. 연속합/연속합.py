n=int(input())
numbers=list(map(int,input().split()))

max_value=first_value=numbers[0]

for i in numbers[1:]: # 1번 값만 빼고 순환
    first_value=max(i,first_value+i) #
    max_value=max(max_value,first_value)

print(max_value)