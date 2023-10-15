def solution(code):
    answer = ''
    mode=0   
    for idx in range(len(code)):
        if mode==0:
            if idx%2==0 and code[idx]!='1':
                answer+=code[idx]
            elif code[idx]=='1':
                mode=1
        elif mode==1:
            if idx%2==1 and code[idx]!='1':
                answer+=code[idx]
            elif code[idx]=='1':
                mode=0
    
    if len(answer)==0:
        answer="EMPTY"
    return answer

print(solution("abc1abc1abc"))