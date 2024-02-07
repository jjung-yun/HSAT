import datetime

# 사용자로부터 시간과 분을 입력받습니다.
hour = int(input("시간을 입력해주세요: "))
minute = int(input("분을 입력해주세요: "))

# 입력받은 시간과 분으로 datetime 오브젝트를 생성합니다.
time = datetime.datetime(2024, 2, 6, hour, minute)

# 원하는 시간(45분)을 빼줍니다.
new_time = time - datetime.timedelta(minutes=45)

# 결과를 출력합니다.
print("{} {}".format(new_time.hour, new_time.minute))