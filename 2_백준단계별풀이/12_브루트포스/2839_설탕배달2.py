N=int(input())
ans=-1

# x 값은 외부 루프에서 결정되며, 각 x에 대해 모든 y 값이 내부 루프에서 탐색됩니다. 
# 따라서, x가 먼저 탐색되고, 그 다음에 각 x에 대한 y가 탐색됩니다.

# 그러나 아래 같은 경우, break가 for 구문 1개만 빠져나옴.
# 그래서 결국 x가 가장 큰 값이 될 때 ans값이 초기화됨.
for x in range(N//5+1):
    for y in range(N//3+1):
        if 5*x+3*y==N:
            ans=x+y
            break
print(ans)