# N개의 숫자들이 주어졌을 때, 적절하게 숫자 K를 선택하여 입력
# 주어진 숫자들 중 K 전부 제외했을 때 연속하여 동일한 숫자가 나오는 횟수가 최대
# 숫자 k는 입력으로 주어진 숫자 중 하나
import sys
from collections import Counter
input = sys.stdin.readline
N=int(input()) # N개의 숫자
arr=[int(input()) for _ in range(N)]
num=Counter(arr)
ans=[]
if(len(set(arr))==1):
    print(0)
else:
    dic=dict()
    for i in arr:
        cnt=1
        remove_set={i}
        temp = [i for i in arr if i not in remove_set]
        for j in range(1,len(temp)):
            if (arr[j]!=i):
                x=temp[j-1]
                if temp[j]==x:
                    cnt+=1
                else:
                    ans.append(cnt)
                    cnt=1
    res= max(ans)
    print(res)


# from collections import Counter
# input = sys.stdin.readline
# N=int(input()) # N개의 숫자
# arr=[int(input()) for _ in range(N)]
# num=Counter(arr)
# ans=[]
# if(len(set(arr))==1):
#     print(0)
# else:
#     dic=dict()
#     for i in arr:
#         cnt=1
#         remove_set={i}
#         temp = [i for i in arr if i not in remove_set]
#         for j in range(1,len(temp)):
#             x=temp[j-1]
#             if temp[j]==x:
#                 cnt+=1
#             else:
#                 ans.append(cnt)
#                 cnt=1
#     res= max(ans)
#     print(res)



