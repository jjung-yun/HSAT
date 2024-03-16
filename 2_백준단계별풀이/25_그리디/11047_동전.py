N,K=map(int,input().split())
money=[]
for _ in range(N):
    money.append(int(input()))

cnt=0

# 가치가 큰 동전부터 확인하기 위해 reverse
for coin in reversed(money):
    if K>=coin:
        cnt+=K//coin #현재 동전으로 만들 수 있는 최대개수
        K%=coin #남은 금액

print(cnt)