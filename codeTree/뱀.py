import sys
input= sys.stdin.readline
n = int(input()) # 보드 크기
k = int(input()) # 사과 개수
apples = [list(map(int, input().split())) for _ in range(k)]
apples.sort() # 사과 정렬
l = int(input()) # 뱀 방향 변환
snake = [list(map(str, input().split())) for _ in range(k)]
nx,ny=1,1
i=0
while True:
    if nx==n or ny==n:
        break
    #
    for j in snake:
        if i==j[0]:
            if(j[1]=="D"):
                nx+=1
            else:
                ny+=1
    print(i)
    


