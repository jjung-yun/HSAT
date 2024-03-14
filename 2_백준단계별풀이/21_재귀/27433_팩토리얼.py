def fact(number):
    # 탈출조건 명확히
    if number==0 or number==1:
        return 1
    # 재귀는 return에 작성
    else:
        return number*fact(number-1)

n=int(input())
print(fact(n))