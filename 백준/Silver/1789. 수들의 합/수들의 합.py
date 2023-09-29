import math

def max_natural_number_count(S):
    # 이항 부등식의 해를 이용하여 N*(N+1)/2 <= S를 만족하는 최대 정수 N을 찾습니다.
    # 여기서 (-1 + sqrt(1 + 8*S)) / 2은 위 부등식의 양의 근입니다.
    return int((-1 + math.sqrt(1 + 8*S)) // 2)

S = int(input())
print(max_natural_number_count(S)) 