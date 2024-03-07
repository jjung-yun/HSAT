#1157 위 문제 딕셔너리 풀이
word=input().upper()

# 딕셔너리를 사용하여 단어의 빈도 세기
word_count={}
for i in word:
    if i in word_count:
        word_count[i]+=1
    else:
        word_count[i]=1

# word_counts 딕셔너리의 가장 큰 value를 가지는 key를 출력
max_key=max(word_count,key=word_count.get)
max_key=max(word_count) # value들 중 최대값을 가진 key

# 최대값이 여러개일 때는 ? 출력
max_value=max(word_count.values()) # 전체 value들 리스트에서 최대값
max_keys = [k for k, v in word_count.items() if v == max_value]  # 최대값을 가지는 모든 key

# 최대값이 여러개일 때는 ? 출력
if len(max_keys) > 1:
    print('?')
else:
    print(max_keys[0])
