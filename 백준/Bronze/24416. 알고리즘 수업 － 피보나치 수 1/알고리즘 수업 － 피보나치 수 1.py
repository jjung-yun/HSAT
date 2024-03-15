# 기존 코드는 함수가 호출될 때마다 cnt+=1 이었음.
# 재귀, DP 둘 다 계산을 위해서는 함수를 2번 호출함 (전전값+전값) => 알고리즘 실행횟수가 아닌 함수 호출 횟수임.

# 문제를 보면 재귀는 return 1이 몇번되었는지, DP는 전전값+전값이 몇 번 실행되었는지를 세라고 적혀있음.

cntR=0
def fiboR(number):
    global cntR
    
    if number==1 or number==2:
        cntR+=1 # 코드1 : 원하는/count할 부분 호출 시 
        return 1
    else: 
        return fiboR(number-2)+fiboR(number-1)
    
def fibo_dp(number):
    memo=[0 for _ in range(number+1)]
    memo[0]=0
    memo[1]=1
    memo[2]=1 #이거까지 하라고 의사코드에 나와있음.
    cntD=0 # 0,1,2 일때 코드2가 아예 안 돔.
    for i in range(3,number+1): # 3~number
        memo[i]=memo[i-2]+memo[i-1] #코드2 : 얘가 돈 횟수를 세는거임.
        cntD+=1
    return cntD

n=int(input())
fiboR(n)
print(cntR,fibo_dp(n))