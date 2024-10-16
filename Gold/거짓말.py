import sys
from collections import deque

# 사람의 수 n과 파티의 수 m
n, m = map(int, input().split())

# 진실을 아는 사람의 수와 번호
truth_knowing_count, *truth_knowing_people = map(int, input().split())

# 각 파티의 정보 저장
parties = []
for _ in range(m):
    party_info = list(map(int, input().split()))
    party_people = party_info[1:]  # 첫 번째 값(인원 수)을 제외
    parties.append(party_people)

def bfs(start, visited):
    que = deque([start])
    while que:
        v = que.popleft()
        if not visited[v]:
            visited[v] = True
            for party in parties:  # 모든 파티를 확인
                if v in party:  # 현재 사람 v가 파티에 있는 경우
                    for person in party:  # 파티의 모든 사람 확인
                        if not visited[person]:
                            que.append(person)

# 진실을 아는 사람이 없을 경우
if truth_knowing_count == 0:
    print(m)  # 모든 파티에서 과장된 이야기를 할 수 있음
else:
    visited = [False] * (n + 1)  # 파티 독립적으로 실행해야 하므로 실행할 때마다 초기화 시켜줌 
    for person in truth_knowing_people:
        bfs(person, visited)  # 진실을 아는 사람으로 BFS 수행

    count = 0
    for party in parties:
        if not any(visited[person] for person in party):  # 진실을 아는 사람이 없는 파티
            count += 1

    print(count)