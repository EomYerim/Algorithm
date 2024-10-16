# from collections import deque


# def bfs(i,j):
#     sh=0
#     wo=0

#     queue=deque()
#     queue.append((i,j))
#     if d[i][j]=="o":
#         sh+=1

#     if d[i][j]=="w":
#         wo+=1

#     d[i][j]="#"

#     while queue:
#         a,b=queue.popleft()
#         for i in range(4):
#             nx=a+dx[i]
#             ny=b+dy[i]
#             if 0>nx or nx>=R or ny<0 or ny>=C and d[nx][ny]!="#":
#                 if d[nx][ny]=="o":
#                     sh+=1
#                 if d[nx][ny]=="v":
#                     wo+=1
#                 d[nx][ny]="#"
#                 queue.append((nx,ny))


#     if wo >= sh:
#         return 0, wo
#     elif sh > wo:
#         return sh, 0
# dx=[0,0,1,-1]
# dy=[1,-1,0,0]
# s=0
# w=0
# d=[]
# R,C=map(int,input().split(" "))
# for i in range(R):
#     d.append(list(map(str,input().split(" "))))
# for i in range(R):
#     for j in range(C):
#         if d[i][j] in 'ov':
#             tmpS,tmpW=bfs(i,j)
#             s+=tmpS
#             w=tmpW
# print(s,w)


from collections import deque
 
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(i,j):
    sheep = 0 
    wolf = 0
    queue = deque()
    queue.append((i, j))
 
    if graph[i][j] == 'o':
        sheep += 1
    elif graph[i][j] == 'v':
        wolf += 1
    graph[i][j] = '#'
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if  0 >tx or tx>=R and 0>ty or ty>=C or graph[tx][ty] != "#":
                if graph[tx][ty] == 'o':
                    sheep += 1
                elif graph[tx][ty] == 'v':
                    wolf += 1
 
                graph[tx][ty] = '#'
                queue.append((tx, ty))
 
    if wolf >= sheep:
        j=wolf
        return 0,j
    elif sheep > wolf:
        j=sheep
        return j, 0
 
 
R,C= map(int, input().split())
graph = []
 
s = 0 
w = 0
 
for i in range(R):
    graph.append(list(input()))
 
for i in range(R):
    for j in range(C):
        if graph[i][j] in 'ov':
            Sheep, Wolf = bfs(i, j)
            s += Sheep
            w += Wolf
 
print(s, w)