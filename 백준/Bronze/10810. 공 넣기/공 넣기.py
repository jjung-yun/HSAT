N,M=map(int,input().split())
basket=[0 for _ in range(N)]
for _ in range(M):
    i,j,k=map(int,input().split())
    for ball in range(i-1,j):
        basket[ball]=k
print(*basket)