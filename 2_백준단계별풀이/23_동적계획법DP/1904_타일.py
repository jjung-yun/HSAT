n=int(input())

# memo
memo=[0 for _ in range(n+1)] # 1일때 인덱스 1을 쓰기 위해서
memo[0]=1 # 1번째 00을 만들기위해 초기화
memo[1]=1

if n>=2:
    for i in range(2,n+1):
        # 1. memo[i-1]에 나온 뒷 자리에 1을 붙인 경우
        # 2. memo[i-2]에 나온 뒷 자리에 00을 붙인 경우
        memo[i]=memo[i-1]+memo[i-2]

print(memo[n])