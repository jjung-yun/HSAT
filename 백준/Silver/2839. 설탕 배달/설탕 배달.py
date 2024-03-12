N=int(input())
ans=-1
for x in range(N//5+1):
    for y in range(N//3+1):
        if 5*x+3*y==N:
            ans=x+y
            break
print(ans)