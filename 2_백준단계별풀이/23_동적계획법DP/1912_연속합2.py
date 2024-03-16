# memo 행렬에서 필요한 값만 저장하고 필요없는것은 계속 지우기.

n=int(input())
numbers=list(map(int,input().split()))
length=len(numbers)
max_value=max(numbers) # 내가 확인할 max 값.

#memo=[[0 for _ in range(length)]] #1차원으로 필요한 값만 담기로함.
#memo=numbers  => 이러면 아예 같은 값을 참조해, memo를 바꾸면 numbers도 바뀜.

# 초기에 같아야 점화식 가능 => 리스트 값 복사법
memo = [x for x in numbers]  # or memo = numbers.copy()

for i in range(length):
    for j in range(length-i-1):
        memo[j]=memo[j]+numbers[j+1+i]
        if memo[j]>max_value:
            max_value=memo[j]

print(max_value)