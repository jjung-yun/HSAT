N,M=map(int,input().split())
maxV=0
numbers=list(map(int,input().split()))
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            newV=numbers[i]+numbers[j]+numbers[k]
            if newV<=M and newV>maxV:
                maxV=newV
print(maxV)