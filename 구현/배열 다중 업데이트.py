import sys

n, m = map(int, input().split())

# 리스트 a 입력
a = list(map(int, input().split()))

# 질의 입력
k = list(list(map(int, input().split()))for _ in range(m))

# 유형 2에 대한 질의만 처리
for i in k:
    query_sum = 0
    if i[0] == 2:  # 첫 번째 값이 2일 때만 처리
        query_sum=a[i[1]]+a[i[2]]
        print(query_sum)

# 질의 차례로 응답해야 됨!!