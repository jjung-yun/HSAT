# available_table=table=[] => available_table=table 가 서로 참조함!
available_table=[]
table=[]
for _ in range(int(input())):
    a,b=map(int,input().split())
    table.append((a,b,b-a))

# b-a 인 튜플의 3번째 값 기준으로 정렬한다.
table.sort(key=lambda x:x[2])

cnt=0
# available_table에 넣을 수 있는지 => 시간이 상충하지 않는지
for meeting in table:

    # 리스트가 비었음은 not으로 표현
    if not available_table:
        available_table.append(meeting)
        cnt+=1
    else:
        for exist_meeting in available_table:

            # 넣으려는 미팅 끝나는 시간이 모든 존재하는 미팅의 시작