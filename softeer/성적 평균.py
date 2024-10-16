import sys
N,K = map(int,input().split())
score=list(map(int,input().split()))
area = list(list(map(int,input().split())) for _ in range(K))

for i in range(K):
    a,b=area[i][0],area[i][1]
    res=sum(score[a-1:b]) / ((b-a)+1)

    print(f"{round(res,2):.2f}")