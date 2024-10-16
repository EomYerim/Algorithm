import sys

# 자신이 최고라고 생각하는 회원의 수
N,M= map(int,input().split())
weight = list(map(int,input().split()))
member=list(list(map(int,input().split())) for _ in range(M))
total_member=[i for i in range(1,N+1)]
dic=dict()
cnt=0
for a,b in enumerate (weight,start=1):
    dic[a]=b

for i in member:
    if dic[i[0]]>dic[i[1]]:
        cnt+=1
    if i[0] not in total_member:
        cnt+=1
print(cnt)