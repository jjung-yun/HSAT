#11021
ans=[]
n=int(input())
for _ in range(n):
    a,b=map(int,input().split())
    ans.append(a+b)

for i in range(n):
    print(f'Case #{i+1}: {ans[i]}')