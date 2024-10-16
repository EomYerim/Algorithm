# #좌우
# x=[3,-2,3,2,-2,-3,2,-3]
# #상하
# y=[-3,2,-3,-2,3,-2,3,2]


# x=[3,3,-2,2,-3,-3,3,3]
# y=[-2,2,-3,-3,2,-2,-2,2]

# x = [-3, -2, 2, 3, 3, 2, -2, -3]
# y = [2, 3, 3, 2, -2, -3, -3, -2]
# r1,c1=map(int,input().split())
# r2,c2=map(int,input().split())

# res=[]
# cnt=0
# for i in range(8):

#     if x[i]+r1==r2 and y[i]+c1==c2:
#         print(1)
#         break
#     else:
#         nx=x[i]+r1
#         ny=y[i]+c1
#         for j in range(len(x)):
#             print("nx,ny",nx,ny)
#             if i==j:
#                 pass
#             nx+=x[j]
#             ny+=y[j]
#             if nx<0 or nx>=8 or ny<0 or ny>=9:
#                 break
#             else:

#                 cnt+=1
#                 if nx==r2 and ny==c2:
#                     res.append(cnt)
    
# print(res)


# from sys import stdin
# input = stdin.readline
# from collections import deque

# #상이 갈 수 있는 곳
# x = deque([-3, -2, 2, 3, 3, 2, -2, -3])
# y = deque([2, 3, 3, 2, -2, -3, -3, -2])

# # x = (-3, -2, 2, 3, 3, 2, -2, -3)
# # y = (2, 3, 3, 2, -2, -3, -3, -2)

# def bfs():
#     board = [[0] * 9 for _ in range(10)]
#     board[r1][c1] = 1
#     queue = deque([(c1, c1)])
#     while queue:
#         r, c = queue.popleft()    
              
#         for d in range(8):
             
#             xr = r + x[d]
#             yc = c + y[d]
#             if xr<0 or xr>=10 or yc<0 or yc>=9 or board[xr][yc]:
#             #if not (0 <= xr < 10 and 0 <= yc < 9) or board[xr][yc]:
#                 continue
#             visited = True 
#             if not visited:
#                 continue
#             if (xr, yc) == (r2, c2): 
#                 return board[r][c]
#             board[xr][yc] = board[r][c] + 1
#             queue.append((xr, yc))
    
#     return -1 


# r1, c1 = map(int, input().split())  # 상 위치
# r2, c2 = map(int, input().split())  # 왕 위치
# print(bfs())




from sys import stdin
from collections import deque
input = stdin.readline

x = deque([-3, -2, 2, 3, 3, 2, -2, -3])
y = deque([2, 3, 3, 2, -2, -3, -3, -2])

f = {0: ((-1, 0), (-2, 1)),
            1: ((0, 1), (-1, 2)),
            2: ((0, 1), (1, 2)),
            3: ((1, 0), (2, 1)),
            4: ((1, 0), (2, -1)),
            5: ((0, -1), (1, -2)),
            6: ((0, -1), (-1, -2)),
            7: ((-1, 0), (-2, -1))}


def bfs():
    board = [[0] * 9 for _ in range(10)]
    board[r1][c1] = 1
    queue = deque([(r1, c1)])
    while queue:
        xr, xc = queue.popleft()   
        visited = True         
        for d in range(8):
            nr = xr + x[d]
            nc = xc + y[d]
            print("zz",nr,nc)
            if nr<0 or nr>=10 or nc<0 or nc>=9 or board[nr][nc]:
                continue
            for j,k in f[d]:
                print(j)
                print(k)
                if (xr+j, xc+k) == (r2, c2):
                    flag = False   
                    break
            if not visited:
                continue
            if (nr, nc) == (r2, c2):
                return board[xr][xc]
            board[nr][nc] = board[xr][xc] + 1
            queue.append((nr, nc))
            
    
    return -1  


 # 상 위치
r1, c1 = map(int, input().split())
# 왕 위치
r2, c2 = map(int, input().split())
print(bfs())