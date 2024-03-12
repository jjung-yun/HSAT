N=int(input())
cnt=0

for _ in range(N):
    word=input()
    word_set=set(word)
    
    # dictionary 만드는법
    word_dict={key: False for key in word_set}

    # enumerate로 index와 value 동시에 가져오기
    for i,v in enumerate(word):
        if i==0:
            word_dict[v] = True
        else:
            if word[i]==word[i-1]:
                continue
            elif word_dict[v]==False:
                word_dict[v] = True
                continue
            else:
                cnt-=1
                break
    cnt+=1
print(cnt)
