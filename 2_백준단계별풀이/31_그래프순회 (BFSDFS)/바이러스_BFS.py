# BFS는 큐를 사용
from collections import deque

#1. 그래프 input 받기
nodes=int(input())
edges=int(input())

graph=[[] for _ in range(nodes+1)] #노드번호와 인덱스번호 맞추기
for _ in range(edges):
    # 양방향 이동이 가능함. graph[노드번호] -> 갈수있는 노드번호
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


#2. Queue를 이용해 순차적으로 visit하기
visited=[False for _ in range(nodes+1)]

def BFS(graph, start, visited):
    visited[start]=True

    # 2-1. 큐 생성 / 문제 상황에 맞는 count 변수
    queue=deque([start])
    cnt=0

    # 2-2. 큐에 있는 애들 먼저 방문 (순차) => 큐가 빌 때까지 
    while queue:
        # 방문할 노드는 큐에서 popleft / 처음이면 start 밖에 없음.
        v=queue.popleft()

        # 처음이면, start 노드에서 갈 수 있는 모든 노드 먼저 보기 (BFS)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                cnt+=1

                #재귀가 아니고 그 노드에 대해 count도 함
                #queue에 넣음 = 방문함체크
                visited[i]=True
    
    return cnt #값을 반환하면 global 안써도 됨.


#3. 결과
ans=BFS(graph,1,visited)
print(ans)
