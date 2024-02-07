import sys
word=sys.stdin.readline()

# -1이 26개 있는 리스트
location_list = [-1] * 26 

# '-1 -1 -1 -1 ... -1' (안 됨)
location_list = ["-1"*26]

# 리스트 컴프리헨젼
location_list = [-1 for _ in range(26)]

for i in reversed(word):
    