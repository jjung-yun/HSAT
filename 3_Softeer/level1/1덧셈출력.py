n=int(input())

ans=[]
for _ in range(n):
    a,b=map(int,input().split())
    ans.append(a+b)

for i in range(n):
    print('Case #{}: {}'.format(i+1,ans[i]))