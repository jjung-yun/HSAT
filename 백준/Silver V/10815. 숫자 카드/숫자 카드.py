import sys

N = int(sys.stdin.readline())
lst_have = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
lst_check = list(map(int, sys.stdin.readline().split()))

dict1 = {item: True for item in lst_have}
print(*[1 if dict1.get(item) else 0 for item in lst_check])