#10952
ans=[]
while(True):
    a,b=map(int,input().split())
    if a==0 and b==0:
        break
    else:
        ans.append(a+b)
print(*ans)