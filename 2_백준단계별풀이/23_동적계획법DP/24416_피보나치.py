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

cnt=0
def fibo_recursion(number):
    # 함수가 호출될 때 마다 전역변수값을 올리면됨!
    global cnt
    cnt+=1
    if number==0:
        return 0
    elif number==1:
        return 1
    else: 
        return fibo_recursion(number-2)+fibo_recursion(number-1)
    
def fibo_tuple(number):
    if number == 0:
        return (0, 1)  # 피보나치 값과 실행 횟수를 튜플로 반환
    elif number == 1:
        return (1, 1)  # 피보나치 값과 실행 횟수를 튜플로 반환
    else:
        result1, cnt1 = fibo_tuple(number-2)
        result2, cnt2 = fibo_tuple(number-1)
        return (result1 + result2, cnt1 + cnt2 + 1)  # 두 호출의 결과와 실행 횟수를 합산하여 반환


print(fibo_recursion(int(input())),fibo_dp(int(input())))
