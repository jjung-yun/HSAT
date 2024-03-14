# 재귀 호출에 비해 동적 계획법이 얼마나 빠른지 확인해 봅시다.
def fibo_dp(number):
    # DP에서 이후값을 구할 때 사용할 이전 값을 행렬에 저장하는 것을 메모이제이션(Memoization)이라 함.
    # 메모이제이션(memoization)
    memo=[0 for _ in range(number+1)]

    # 이후 계산에 도움을 줄 초기값 n=0, n=1값 설정
    memo[0]=0
    memo[1]=1
    cnt=1
    # n=2부터 n=number 까지 값 계산
    for i in range(2,number+1): # 2~number
        memo[i]=memo[i-2]+memo[i-1]
        cnt+=1
    
    # 초기값들로 만들어진 결과값 number번째 값 반환
    #return memo[number]
        
    # 실행횟수를 반환
    return cnt

def fibo_recursion(number):
    cnt=0
    if number==0:
        cnt+=1
        return 0,cnt
    elif number==1:
        cnt+=1
        return 1,cnt
    else: 
        cnt+=1
        return fibo_recursion(number-2)[0]+fibo_recursion(number-1)[0]

fibo_recursion(int(input()))
ans_dp=fibo_dp(int(input()))
print(,)
