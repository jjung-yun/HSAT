# 안 보고 BFS 구현하기
from collections import deque

graph = [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

# BFS 구현 함수
def BFS(x,y,visited):
    # 시작 노드 넣고 방문처리
    queue = deque([(x,y)]) # deque() 안에 리스트를 넣어야하고, 리스트 값으로 튜플
    visited[x][y]=True

    # 상하좌우 확인할 노드 인덱스
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    # 큐가 빌 때까지 상하좌우 노드들을 확인
    while queue:
        # 처음 값 뿐 아니라 queue 넣은 x,y값도 사용하고 쓴 값은 제거.
        x,y = queue.popleft() # BFS이므로 왼쪽에서 뽑기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # case 1. 상하좌우 노드가 그래프를 벗어나면 x
            if nx<0 or ny<0 or nx>=len(graph) or ny>=len(graph[0]):
                continue 
            # case 2. 상하좌우 노드 값이 1이거나 방문했으면 x
            if graph[nx][ny]==1 or visited[nx][ny]:
                continue

            # 위 케이스가 아니면 큐에 넣고 방문처리
            queue.append((nx,ny))
            visited[nx][ny]=True

def solve():
    #초기화
    visited=[[False]*len(graph[0]) for _ in range(len(graph))]
    count=0

    # 적합한 모든 노드에서 BFS
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j]==0 and not visited[i][j]: # 0이고 방문 안한 노드
                BFS(i,j,visited)
                count+=1
    return count

print(solve())