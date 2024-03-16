n=int(input())
minimum=float('-inf') # int와 float의 메모리차이는 굉장히 미미함.
numbers=list(map(int,input().split()))
length=len(numbers)

# 2차원 배열 이렇게 만들면 안됨.
#memo=[[minimum for _ in range(length)]*length]
memo=[[minimum for _ in range(length)]for _ in range(length)]

memo[0] = numbers[:] # 1차원 배열을 2차원 배열의 첫 번째 행에 할당

for i in range(1,length):
    for j in range(length-1,i,-1):
        memo[i][j]=memo[i-1][j]+memo[0][j-i] #뒤에 더해지는 값은 기존 정해진 값에 다음값


# 각 내부 리스트의 최대값을 찾고, 그 중에서 최대값을 찾음
max_value = max(max(row) for row in memo)
print(max_value)