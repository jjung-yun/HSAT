x,y=map(int,input().split())
chess=[]
for _ in range(y):
    chess.append(input())

#보드 전체순회
for i in range(x-7):
    for j in range(y-7):
        # 처음이 B, W에 따른 변화를 같이 세기.
        black_change=0
        white_change=0
        
        # 8x8 내의 보드에서 뭐가 빠른지 세기
        for k in range(8):
            for l in range(8):
                # B로 시작하는경우
                if (i+k)%2!=0 and (j+l)%2!=09
                chess[i+k][j+l]