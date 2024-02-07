import sys
number=int(sys.stdin.readline())
score_list=list(map(int,sys.stdin.readline().split()))
max_score=max(score_list)

# 리스트 컴프리헨션을 사용
normalized_scores=[(score/max_score)*100 for score in score_list]

# map함수를 이용 => map의 첫번째인자는 함수니까 람다함수를 사용해 연산.
normalized_scores = list(map(lambda score: (score / max_score) * 100, score_list))

# 파이썬은 정수 정수 나눠도 자동으로 실수가 되므로 float() 안 써도 됨
average = sum(normalized_scores) / len(normalized_scores)
print(average)
