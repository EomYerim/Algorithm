import sys
input = sys.stdin.readline
n,m=map(int,input().split(" "))
a=list(map(int,input().split(" ")))
b=[int(input()) for _ in range(m)] # 각 원소보다 큰 값을 찾아야 함

for i in b:
    cnt=0
    for j in a:
        if j>=i:
            cnt+=1
    print(cnt)