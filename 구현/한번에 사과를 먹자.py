import sys

def solution(board, r, c):
    # 4방향 (상, 하, 좌, 우)
    dd = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
    # 사과가 있는지 확인
    for dr, dc in dd:
        # 새로운 위치 계산
        nr = r + dr
        nc = c + dc
        # 범위 체크 후 사과 확인
        if in_range(nr, nc) and board[nr][nc] == 1:
            return 1
    
    return 0

def in_range(nr, nc):
    # 좌표가 보드의 범위 내에 있는지 확인
    return 0 <= nr < 5 and 0 <= nc < 5

# 입력 처리
board = list(list(map(int, input().split())) for _ in range(5))
r, c = map(int, input().split())

# 결과 출력
print(solution(board, r, c))