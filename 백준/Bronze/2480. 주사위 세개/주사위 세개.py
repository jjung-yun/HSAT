# 2480: 같은 수의 개수는 집합을 이용!
dices=list(map(int,input().split()))
dices.sort() #가장 큰 수를 써야하니 정렬

if len(set(dices))==1:
    print(10000+dices[0]*1000)
elif len(set(dices))==2:
    # if dices[0]==dices[1]: # 경우가 앞/뒤 같은지 2개 뿐임 (정렬상태)
    #     print(1000+dices[0]*100)
    print(1000+dices[1]*100) #정렬 상태니 중간은 무조건 같은 값
else:
    print(100*dices[2])
    