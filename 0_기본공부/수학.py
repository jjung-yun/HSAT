import math

#해당 기호 ⌊ ⌋는 수학에서 '내림(floor)' 값을 의미

# math 모듈의 floor 함수를 사용하는 방법
p = 5
r = 3
q = math.floor((p + r) / 2)
print(q) # 결과: 4


#파이썬의 내장 함수인 // 연산자를 사용하는 방법. 이 연산자는 나눗셈의 결과를 내림하여 정수로 반환합니다.
p = 5
r = 3
q = (p + r) // 2
print(q) # 결과: 4

#올림 :  ⌈ ⌉ 기호를 사용
p = 5
r = 3
q = math.ceil((p + r) / 2)
print(q) # 결과: 4