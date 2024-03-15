#memoization
# memo=[1 for _ in range(-50,51)] => 이게 아님.



def w(a,b,c):
    # 이미 계산된 값이 있으면 반환 => DP의 핵심.
    if (a,b,c) in memo:
        return memo[(a,b,c)]
    
    # 값을 아는거면 바로 반환
    if a<=0 or b<=0 or c<=0:
        return 1
    elif a>20 or b>20 or c>20:
        return w(20,20,20)

    # 모르는 값은 memo (나중에 쓸 거) => DP 핵심을 위해 memo
    elif a<b and b<c:
        memo[(a,b,c)]=w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c)
        return memo[(a,b,c)] # 값을 바꿔주고 반환해줘야 실제 memo가 달라짐.
    else:
        memo[(a,b,c)]=w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
        return memo[(a,b,c)]

while True:
    a,b,c=map(int,input().split())
    if a==-1 and b==-1 and c==-1:
        break
    # dictionary
    memo={}
    ans=w(a,b,c) #w(a,b,c)의 반환값은 int임
    print(f'w({a}, {b}, {c}) = {ans}')