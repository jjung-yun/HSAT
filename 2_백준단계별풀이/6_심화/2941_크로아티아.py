word=input()
cnt=len(word)
for i in range(cnt):
    if i==0:
        continue
    else:
        pre=i-1
        if word[i]=='=':
            if word[pre]=='c' or word[pre]=='s':
                cnt-=1
            elif word[pre]=='z':
                if word[pre-1]=='d':
                    cnt-=2
                else:
                    cnt-=1
        elif word[i]=='-':
            if word[pre]=='c' or word[pre]=='d':
                cnt-=1
        elif word[i]=='j':
            if word[pre]=='l' or word[pre]=='n':
                cnt-=1
print(cnt)