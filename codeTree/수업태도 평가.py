# 첫 줄에 수업 태도 점수가 두 번째로 낮은 학생의 이름을 출력합니다.

# 만약 수업 태도 점수가 가장 낮은 학생이 여러 명이라면, 그다음으로 낮은 점수를 갖는 학생의 이름을 출력해야 합니다.
# min이 여러명이라면 그 다음으로 차순 넘어감 

# 만약 두 번째로 낮은 점수를 갖는 학생이 여러 명이거나, 모든 학생의 점수가 같다면, Tie를 출력합니다.


import sys
input = sys.stdin.readline
from collections import Counter

N =int(input())
students=[input().rsplit() for i in range(N)]
result = {}
if N==1:
    print(students[0][0])
else:
    scores = Counter()
    for name, score in students:
        scores[name] += int(score)
#min이 여러개면 차순위, 차순위 개수도 여러개면 Tie, 
# 최소값 찾기
    min_value = min(scores.values())
    max_value = max(scores.values())
    if(min_value==max_value):
        print("Tie")
    else:
        res = Counter({k: v for k, v in scores.items() if v > min_value})
        result_min_value = min(res.values())
        min_keys = [k for k, v in res.items() if v == result_min_value]

        # 최소값을 가진 키의 개수 확인
        if len(min_keys) > 1:
            print("Tie")
        else:
            print(min_keys[0])


# import sys
# input = sys.stdin.readline
# N =int(input())
# stdents=[input().rsplit() for i in range(N)]
# result = {}
# if N==1:
#     print(stdents[0][0])
# else:
#     for k, v in stdents:
#         result[k] = result.get(k, 0) + int(v)
#     scores = sorted(list(result.values()),reverse=False) #점수들 기준 check
#     if(scores.count(scores[1])==N-1) :
#         print("Tie")
#     else:
#         # 그 다음으로 낮은 학생 출력
#         if scores.count(scores[0])>1:
#                 remove_set={scores[0]}
#                 scores = [i for i in scores if i not in remove_set]
#         for key, value in result.items():
#             if value ==scores[0]:
#                 if scores.count(scores[0])==1: 
#                     print(key)
#                 else:
#                     print("Tie")