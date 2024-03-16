#1. graph, 방문 행렬
graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited=[False] * 9


#2. DFS
def DFS(graph,v,visited):
    visited[v]=True
    print(v, end=' ')  # 방문한 노드 순서대로 출력

    # v라는 노드부터 depth 적으로 연결된 모든 애
    for i in graph[v]:
        if not visited[i]: #v번째 노드에서 연결된 노드들 중 방문하지 않은 것들
            DFS(graph,i,visited) # 재귀로 들어감. => 함수내에서 visited 체크됨.

DFS(graph,1,visited)
print(visited) # 아예 바껴있음.


#3. BFS

print('BFS case')
visited=[False] * 9

from collections import deque

def BFS(graph, start, visited):
    # 큐 만들어서 큐 빌 때까지 앞에꺼 빼고 연결된애들 중 방문안한애들 방문처리 후 큐에 다 넣기 반복.
    # 1. 큐만듦
    queue=deque([start])

    # 2. 빌때까지 앞에꺼 빼고
    while queue:
        v=queue.popleft()
        print(v,end=' ') # 방문한 노드 프린트하기.

        # 3. 연결된애 노드 번호 찾기
        for i in graph[v]:
            
            # 4. 방문안한애들만 방문처리+큐넣기
            if not visited[i]:
                visited[i]=True
                queue.append(i)

BFS(graph,1,visited)