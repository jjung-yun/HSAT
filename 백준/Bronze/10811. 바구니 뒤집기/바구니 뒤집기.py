# 10811 리스트 뒤집기
N,M=map(int,input().split())
basket=[i+1 for i in range(N)]
for _ in range(M):
    start,end=map(int,input().split())
    basket[start-1:end]=basket[start-1:end][::-1]
print(*basket,sep=' ')