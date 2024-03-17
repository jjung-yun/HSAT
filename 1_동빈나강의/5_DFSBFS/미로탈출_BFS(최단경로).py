N,M=5,6

graph=[ #[y]에 '101010' 문자열로 들어오는거는 list(map(int,input())) 으로 행렬화해야함!
    [1,0,1,0,1,0],
    [1,1,1,1,1,1],
    [0,0,0,0,0,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1],
]

#visited=[[False for _ in range(M)] for _ in range(N)]

from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]

# 최단경로 문제 => 2차원 x,y 값을 input
# visited를 기록하지 않고, 처음 방문하는 노드, 방문할 수 잇는 노드의 횟수만 세기.
# graph파라미터 없어도 됨. => 반환한 값이 그대로 글로벌로 적용됨.
# graph가 여러개 나오는 경우 BFS에 graph를 넣어줘야함!

distance=0
def BFS(x,y):
    #1. 빈 큐 생성
    queue=deque()

    #2. 큐에 초기값 => 튜플로
    queue.append((x,y))

    #3. 그 값에 연결된 가능한 방향 탐색(상하좌우)
    while queue:
        # 상하좌우 케이스를 봄 => next case
        # (1)테두리 벗어나면 끝 / (2)갈 수 없는 곳이면 (==0) 끝 / 둘 다 아니면 갈 수 잇는경우 => 거리측정+그 노드를 큐에 넣음.

        # 큐에서 x,y값을 뽑아와 써야하기 때문에.
        x,y=queue.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue #다른 방향 확인
            if graph[nx][ny]==0: # 못가는방향 / elif 아니어도 됨.
                continue
            if graph[nx][ny]==1: # 원하는 케이스 + 방문안 함. => 방문한 케이스는 거리값으로 바꿨기 때문.
                #distance+=1 상하좌우 다 갈 수 잇는 케이스의 모든 distance는 똑같아야함.

                # 증가된 거리에 따라 next값은 현재값보다만 1 높으면 됨.
                graph[nx][ny]=graph[x][y]+1 
                queue.append((nx,ny))

    # 그림 (1,1) 은 행렬인덱스에서 (0,0) 이므로 원하는 위치 (n,m)은 행렬에서 (n-1,m-1)이다.
    return graph[N-1][M-1]

print(BFS(0,0))