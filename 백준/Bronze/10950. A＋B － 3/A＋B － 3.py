#10950
ans=[]
for i in range(int(input())):
    a,b=map(int,input().split())
    ans.append(a+b)
print(*ans,sep='\n')