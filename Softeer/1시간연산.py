from datetime import datetime
ans=0
for _ in range(5):
    t1,t2=input().split()
    diff=datetime.strptime(t2,'%H:%M')-datetime.strptime(t1,'%H:%M')

    ans+=int(diff.total_seconds()/60)

print(ans)
