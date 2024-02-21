#2525
now_hour,now_minute=map(int,input().split())
step=int(input())

add_minute=now_minute+step
add_hour=add_minute//60
result_hour=now_hour+add_hour
result_minute=add_minute%60
print(result_hour if result_hour<24 else result_hour-24, result_minute)