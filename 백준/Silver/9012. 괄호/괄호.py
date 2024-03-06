# (면 +1)면 -1  해서 총 0이면 VPS
# )가 먼저 나와서 -1 되면 X
ans_list=[]
for _ in range(int(input())):
    lst=list(input())
    ans=0
    flag=False
    for i in lst:
        if i=='(':
            ans+=1
        else:
            ans-=1
        
        if ans<0:
            ans_list.append('NO')
            flag=True
            break
    if ans==0 and flag==False:
        ans_list.append('YES')
    elif flag==False:
        ans_list.append('NO')
        
print(*ans_list,sep='\n')