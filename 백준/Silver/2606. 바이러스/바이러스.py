#1. input받아 그래프 만들기.
com=int(input()) # node
net=int(input()) # edge

graph=[[] for _ in range(com+1)] # 노드수+1 : 인덱스=노드번호
for _ in range(net):
    a,b=map(int,input().split())
    # 바이러스는 양방향으로 퍼지므로
    graph[a].append(b)
    graph[b].append(a)


#2. DFS로 그래프 순회
visited=[False for _ in range(com+1)] # 인덱스=노드번호
count=0

def DFS(graph, v, visited):
    visited[v]=True
    global count #1번 노드 (v=1)에서 연결되고 거기서 또 연결되는 모든 노드들 세는 변수

    # v=1으로 시작 시 1번과 연결된 노드들 중 방문 안한거 개수세기 + 걔네들로 연결된 애들 DFS
    for i in graph[v]: #v와 연결된 애들
        if not visited[i]:
            DFS(graph,i,visited) #방문 안한 노드부터 연결된 방문안한 노드들을 탐색
            count+=1 


# 3. 원하는 노드부터 실행결과 출력
DFS(graph,1,visited)
print(count)