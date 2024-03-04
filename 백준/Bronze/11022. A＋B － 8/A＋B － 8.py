#11021
ans=[]
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    ans.append(f'Case #{i+1}: {a} + {b} = {a+b}')

print(*ans)