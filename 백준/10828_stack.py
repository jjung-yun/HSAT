N=int(input())

lst=[]
ans=[]
for i in range(0,N):
    _list=list(input().split())
    if _list[0]=='push':
        lst.append(int(_list[1]))
    elif _list[0]=='pop':
        if len(lst)==0:
            ans.append(-1)
        else:
            ans.append(lst[-1])
            lst.pop()
    elif _list[0]=='size':
        ans.append(len(lst))
    elif _list[0]=='empty':
        if len(lst)==0:
            ans.append(1)
        else:
            ans.append(0)
    else:
        if len(lst)==0:
            ans.append(-1)
        else:
            ans.append(lst[-1])

print(*ans,sep='\n')