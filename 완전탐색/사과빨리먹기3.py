# # 현재 위치에서 상,하,좌,우 방향으로 이동하여 사과 3개 먹을 수 있는지 체크, 최소 이동 횟수
# # 상하좌우 방향으로 이동할 때 현재 위치를 장애물로 변경하여 재귀함수 호출, 재귀 함수가 종료되면 원래 값으로 변경 
# import sys

# def solution(board,aloc):
#     # board : 보드의 초기 상태
#     # aloc : 학생의 현재 위치
#     # 3 : 앞으로 먹어야 할 사과 개수
#     return solve(board,aloc,3)

# def solve(board,aloc,apple_num):
#     #현재 위치에서 사과를 먹기 위한 최소 이동 횟수 반환
#     #사과를 먹을 수 없는 경우 -1 반환
#     if apple_num==0:
#         return 0 # 사과를 다 먹은 경우 추가 이동 필요 없음 
    
#     ret = -1 #현재 위치에서 사과를 먹기 위한 최소 이동 횟수 초기값 : -1

#     #상하좌우 방향으로 모두 시도
#     dd=[[-1,0],[1,0],[0,-1],[0,1]]
#     for dr,dc in dd:
#         r,c=aloc[0]+dr,aloc[1]+dc
#         if in_range([r,c]) and board[r][c]!=-1:
#             # 현재 위치에 있는 값을 pre_value 저장
#             prv_value=board[aloc[0]][aloc[1]]
#             # 현재 위치를 장애물 위치로 변경
#             board[aloc[0]][aloc[1]]=-1

#             # 다음 이동 위치인 (r,c) 이동, 사과를 먹을 수 있는 경우 현재의 1회 이동을 반영
#             cur_ret = solve(board,[r,c],apple_num-board[r][c])
#             if cur_ret!=-1:
#                 cur_ret+=1

#             if cur_ret!=-1:
#                 if ret ==-1 or cur_ret<ret:
#                     ret = cur_ret
#             board[aloc[0]][aloc[1]] = prv_value
#     return ret 



# def in_range(loc):
#     return 0<=loc[0]<=4 and 0<=loc[1]<=4

# board=list(list(map(int,input().split(" ")))for _ in range(5))
# aloc=list(map(int,input().split()))
# print(solution(board,aloc))


# # def checkBoard(board,r,c):
# #     dd=[[-1,0],[1,0],[0,-1],[0,1]]
# #     # 상,하,좌,우 이동
# #     for dr,dc in dd:
# #         nr=dr+r
# #         nc=dc+c
# #         if(count==3):
# #             res.append(move)
# #         if(in_board(nr,nc) and board[nr][nc]==1):
# #             count+=1
# #             board[nr][nc]=-1
# #             checkBoard(board,nr,nc)
# #         elif(in_board(nr,nc) and board[nr][nc]==-1):
# #             break
# #         move+=1

# #     return res

# # def in_board(r,c):
# #     return 0<=r<=4 and 0<=c<=4
 


    

# # board=list(list(map(int,input().split(" ")))for _ in range(5))
# # r,c=map(int,input().split())
# # res=[]
# # count=0
# # move=0
# # print(checkBoard(board,r,c))


import sys
input = sys.stdin.readline

l = []
for i in range(5):
    l.append(list(map(int, input().split())))
    
r, c = map(int, input().split())

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
answer = []
apple = dis = 0

def dfs(l, r, c, dis, answer):
    global apple
    if(apple == 3):
        answer.append(dis)
    
    for i in range(4):
        new_r = r + dxy[i][0]
        new_c = c + dxy[i][1]
        
        if(0 <= new_r < 5 and 0 <= new_c < 5 and l[new_r][new_c] != -1):
            
            if(l[new_r][new_c] == 1):
                apple += 1
            
            temp = l[r][c]
            l[r][c] = -1
            dfs(l, new_r, new_c, dis + 1, answer)
            l[r][c] = temp
            
            if(l[new_r][new_c] == 1):
                apple -= 1
            
    return answer            

if(dfs(l, r, c, dis, answer)):
    print(min(answer))
else:
    print(-1)