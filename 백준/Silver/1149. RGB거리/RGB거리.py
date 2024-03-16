import sys

n=int(sys.stdin.readline())

cost=[]
for _ in range(n):
    cost.append(list(map(int,sys.stdin.readline().split())))

memo=[[0 for _ in range(3)]for _ in range(n)]

# 초기값 shallow copy 해 넣기.
memo[0]=cost[0][:]

# DP로 값구하기 (memo는 cost의 총합)
for i in range(1,n):
    # 현재값이 R인경우 => G, B중 낮은값 + R의 cost
    memo[i][0]=min(memo[i-1][1],memo[i-1][2])+cost[i][0]

    memo[i][1]=min(memo[i-1][0],memo[i-1][2])+cost[i][1]
    memo[i][2]=min(memo[i-1][0],memo[i-1][1])+cost[i][2]

print(min(memo[n-1]))