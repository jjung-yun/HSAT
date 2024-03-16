# memo
memo=[0,1,1,1,2,2,3,4,5,7,9]

def wave(n):
    if n<=10:
        return memo[n] # 일부러 인덱스0 에 0 추가
    else:
        for i in range(11,n+1):
            if len(memo)>i:
                continue
            else:
                memo.append(memo[i-1]+memo[i-5])
        return memo[n]

for _ in range(int(input())):
    print(wave(int(input())))
