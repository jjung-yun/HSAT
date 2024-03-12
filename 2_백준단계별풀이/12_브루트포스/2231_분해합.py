n=input()
number=int(n)
radix=len(n)

for i in range(0,number+1): #10**(radix-2)
    ans=0
    if i==number: # number 까지 보기 위해서는 number+1을 해줘야함.
        print(0)
        break
    ans+=i
    for j in str(i):
        ans+=int(j)
    if ans==number:
        print(i)
        break