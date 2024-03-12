from itertools import combinations

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
maxV = 0

# numbers 리스트에서 3개의 수를 선택하는 모든 조합을 생성
for comb in combinations(numbers, 3):
    newV = sum(comb)  # 선택된 3개의 수의 합
    if newV <= M and newV > maxV:
        maxV = newV

print(maxV)
