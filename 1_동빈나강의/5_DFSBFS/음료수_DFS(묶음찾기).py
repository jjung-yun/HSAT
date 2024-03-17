lst=[[0,0,1,1,0],
     [0,0,0,1,1],
     [1,1,1,1,1],
     [0,0,0,0,0]]

# dirX=[1,-1,0,0]
# dirY=[0,0,1,-1]

def DFS(x,y):
    # DFS를 확인할 위치가 범위를 벗어나면 종료 (인덱스를 활용)
    if x<=-1 or x>3 or y<=-1 or y>4:
        return False

    # 방문한지 확인 후 아니면 DFS (lst를 활용)
    if lst[x][y]==0:
        lst[x][y]=1 #count만 할 거니 값 넣어도 됨.

        # 4방향 DFS
        DFS(x+1,y)
        DFS(x-1,y)
        DFS(x,y+1)
        DFS(x,y=1)

        # 방문하지 않았고 잘 수행되었으면 True를 
        return True
    
    # 이미 방문을 했다면 False를
    return False

cnt=0

# 모든 노드를 방문한뒤 DFS가 실행된 횟수가 얼음의 개수임.
for i in range(4):
    for j in range(5):
        if DFS(i,j)==True: # 방문하게 되면 그 얼음 덩어리는 모두 1이 됨. => 방문가능한 횟수가 덩어리 개수.
            cnt+=1
print(cnt)