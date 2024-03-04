#10951
#반복문의 종료 조건이 없을 때는 try, except 구문을 사용한다.
while(True):
    try:
        a,b=map(int,input().split())
        print(a+b)
    except:
        break
