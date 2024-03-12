def find_min_changes(board, M, N):
    min_changes = float('inf')  # 가능한 최소 변경 횟수를 저장하기 위한 변수 초기화

    # 모든 가능한 8x8 영역에 대해 루프
    for i in range(M - 7):
        for j in range(N - 7):
            changes_white = 0  # 첫 번째 칸이 흰색일 때 필요한 변경 횟수
            changes_black = 0  # 첫 번째 칸이 검은색일 때 필요한 변경 횟수
            # 선택된 8x8 영역 내에서 루프
            for k in range(8):
                for l in range(8):
                    # 현재 칸이 올바른 색인지 확인
                    if (k + l) % 2 == 0:  # 현재 칸이 첫 번째 칸과 같은 색이어야 함
                        if board[i + k][j + l] != 'W': changes_white += 1
                        if board[i + k][j + l] != 'B': changes_black += 1
                    else:  # 현재 칸이 첫 번째 칸과 다른 색이어야 함
                        if board[i + k][j + l] != 'B': changes_white += 1
                        if board[i + k][j + l] != 'W': changes_black += 1
            # 두 경우 중 최소 변경 횟수를 선택
            min_changes = min(min_changes, changes_white, changes_black)

    return min_changes

# 예시 입력
M, N = 10, 13  # 보드의 크기
board = [
    "BBBBBBBBWBWBW",
    "BBBBBBBBBWBWB",
    "BBBBBBBBWBWBW",
    "BBBBBBBBBWBWB",
    "BBBBBBBBWBWBW",
    "BBBBBBBBBWBWB",
    "BBBBBBBBWBWBW",
    "BBBBBBBBBWBWB",
    "WWWWWWWWWWBWB",
    "WWWWWWWWWWBWB"
]

print(find_min_changes(board, M, N))
