# 시간 초과 코드
# from itertools import combinations_with_replacement
# import math
# import sys
# input=sys.stdin.readline
# s,k=map(int,input().split(" "))
# num=[i for i in range(1,s+1)]
# res=[]
# for cwr in combinations_with_replacement(num, k):
#     if sum(list(cwr))==s:
#         res.append(math.prod(list(cwr)))
# print(max(res))


#성공 코드
import math
s,k=map(int,input().split(" "))
num=[i for i in range(1,s+1)]
res=[]
for i in range(k):
    tmp=s//k
    s-=tmp
    k-=1
    res.append(tmp)
print(math.prod(res))