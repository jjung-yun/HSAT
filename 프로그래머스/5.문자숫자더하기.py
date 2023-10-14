def solution(a, b):
    answer = max(int(str(a)+str(b)),int(str(b)+str(a)))
    return answer

print(solution(1,2))