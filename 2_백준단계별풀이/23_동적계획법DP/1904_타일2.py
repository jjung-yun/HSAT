# memo 리스트를 만들지 않고, 튜플로 값을 바꿔서 저장하면 메모리 아낌.

N = int(input())

# 초기 조건 설정
a, b = 1, 1

# N=1일 때, 추가 계산을 방지하기 위한 조건문
for i in range(2, N+1):
    a, b = b, (a + b) % 15746  # a와 b의 값을 갱신하며, 이전 두 값의 합을 계산

# N이 1인 경우 b가 아닌 a를 출력해야 하므로 N에 따라 출력값을 조정
print(b if N > 1 else a)
