import sys # import는 모듈을 뜻함.
from datetime import datetime, time, timedelta # datetime 모듈에서 datetime 클래스를 가져옴.
# import datetime만쓰면 datetime.datetime. 으로 strptime 써야함.

hour,minute=sys.stdin.readline().split()


# 방법1
time_string = ":".join([hour,minute])# 입력 값을 콜론으로 구분된 문자열로 만들기
time_obj = datetime.strptime(time_string, "%H:%M")# datetime 객체 생성

# 방법2 : 연,월,일,시간,분 모두 포함한 데이터
time_obj = datetime.strptime(f"{hour}:{minute}", "%H:%M")

# 방법3 : time 객체는 시간,분,초만 있음.
time_obj = time(int(hour), int(minute))

# 방법4 : 연,월,일,시간,분 모두 포함한 데이터
time_obj = timedelta(hours=int(hour), minutes=int(minute))

#시간 계산
result= time_obj - timedelta(minutes=45)
#print(result) #9:25:00
#print(timedelta.total_seconds(result)) #33900.0

time_obj = datetime.strptime(f"{hour}:{minute}", "%H:%M")
print(datetime.hour)
