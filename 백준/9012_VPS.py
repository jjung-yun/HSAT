ans=[]
for i in range(int(input())):
    lst=input()
    if len(lst)%2==1 or lst[0]==')':
        ans.append('NO')
    else:
        