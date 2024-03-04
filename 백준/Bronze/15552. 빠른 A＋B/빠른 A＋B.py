#15552
ans=[]
for _ in range(int(input())):
    a,b=map(int,input().split())
    ans.append(a+b)
print(*ans, sep='\n')
