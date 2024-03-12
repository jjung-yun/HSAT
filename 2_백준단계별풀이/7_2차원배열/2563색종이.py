# 2차원 리스트 초기화
paper=[[0 for _ in range(100)] for _ in range(100)]

# 색종이 붙이기
for _ in range(int(input())):
    x,y=map(int,input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            paper[i][j]=1

# 색종이 영역 넓이 계산 (2차원 배열의 1 개수 세기): 2차원 배열의 1줄 1줄 count(1)
area=sum(row.count(1) for row in paper)

print(area)