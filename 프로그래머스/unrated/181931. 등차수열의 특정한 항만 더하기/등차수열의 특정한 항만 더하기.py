def solution(a, d, included):
    answer = 0
    lst=[]
    for i in range(a,d*len(included)+a,d):
        lst.append(i)
    for idx, val in enumerate(included):
        if val==True: 
            answer+=lst[idx]
    
    return answer

print(solution(3,4,[True, False, False, True, True]))