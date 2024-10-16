import sys
from collections import defaultdict

# 자신이 최고라고 생각하는 회원의 수
N,M= map(int,input().split())
weight = list(map(int,input().split()))
member=list(list(map(int,input().split())) for _ in range(M))

dic=defaultdict(list)

for a,b in enumerate (member,start=1):
    dic[b[0]].append(b[1])
    dic[b[1]].append(b[0])

count = 0
for i in range(1, N+1):
    # 친구가 없으면 자신이 최고라고 생각
    if not dic[i]:
        count += 1
    else:
        # 친구들보다 무게를 더 많이 들 수 있으면 자신이 최고라고 생각
        if all(weight[i-1] > weight[friend-1] for friend in dic[i]):
            count += 1

print(count)


    