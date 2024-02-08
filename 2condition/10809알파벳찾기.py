import sys
word=sys.stdin.readline()

# -1이 26개 있는 리스트
location_list = [-1] * 26 

# '-1 -1 -1 -1 ... -1' (안 됨)
location_list = ["-1"*26]

# 리스트 컴프리헨젼
location_list = [-1 for _ in range(26)]

# 아스키코드로 바로 풀이
res = [word.find(chr(i)) for i in range(97,123)] #a=97, z=122
#print(' '.join(map(str, res)))

# chr 함수는 정수에 대한 아스키 문자 반환 '97'이면 'a'
# str 함수는 문자열로 반환 

# 문자열 나열해 풀이
alphabet = 'abcdefghijklmnopqrstuvwxyz'
res = [word.find(a) for a in alphabet]
print(' '.join(map(str, res)))