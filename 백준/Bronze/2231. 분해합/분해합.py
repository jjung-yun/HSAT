n=input()
number=int(n)
radix=len(n)

for i in range(0,number): #10**(radix-2)
    ans=0
    if i==number-1:
        print(0)
        break
    ans+=i
    for j in str(i):
        ans+=int(j)
    if ans==number:
        print(i)
        break