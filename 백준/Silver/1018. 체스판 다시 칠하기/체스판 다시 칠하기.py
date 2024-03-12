x,y=map(int,input().split())
chess=[]
for _ in range(x): # y가 아니라 x로 받아야함!!!
    chess.append(input())

#8x8보드에서 흰색으로 바꾸는 것과 검정색으로 바꾸는 것 중 최소값 반환하는 함수
#위 함수의 파라미터로 보드를 넣어줘야하니 귀찮음.

#가장 큰 값
min_changes = float('inf')

#보드 전체순회
for i in range(x-7):
    for j in range(y-7):
        # 처음이 B, W에 따른 변경횟수 세어서 낮은거 찾기. (모든 경우)
        black_change=0
        white_change=0
        
        # 8x8 내의 보드에서 뭐가 빠른지 세기
        for k in range(8):
            for l in range(8):
                # k+l이 홀수는 첫번째인 것과 같아야함.
                if (k+l)%2!=0:
                    #홀수번째를 모두 B로 하고싶다면, W일 때 B로 바꾸면서 흰색바꿈값 증가
                    if chess[i+k][j+l]=='W':
                        #chess[i+k][j+l]='B' #바꾸는 횟수만 세는거니 안바꿔도 될듯
                        white_change+=1
                    else:
                        black_change+=1
                else:
                    #첫번째값과 반대여야함. B라면 white change 증가
                    if chess[i+k][j+l]=='B':
                        white_change+=1
                    else:
                        black_change+=1
                
        #이번 보드에서 나온 B, W 중 최소값과 기존 최소값 중 더 작은걸 선택
        min_changes=min(min_changes,white_change,black_change)
        # B로 바꾸는게 좋은지, W로 바꾸는게 좋은지는 안중요함.
        # 몇번 바꿔야하는지 숫자만 알면됨!
print(min_changes)