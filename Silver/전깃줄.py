import sys
input=sys.stdin.readline
n=int(input())

dp=[1]*n

arr=sorted([list(map(int, input().split())) for _ in range(n)])


for i in range(n):
    for j in range(i):
        if arr[i][1]>arr[j][1]:
            dp[i]=max(dp[i],dp[j]+1)

print(n-max(dp))

# arr=dict()
# up=0
# down=0

# for i in range(n):
#     a,b=map(int,input().split())
#     arr[a]=b
# tmp=0
# s=0
# chk=0
# for i in arr:
#     if tmp<arr[i]: #8 9
#         if i<arr[i]:
#             up+=1 #1 2
#     elif tmp>arr[i]:
#         if i>arr[i]:
#             down+=1 # 1 
#             if i>s:
#                 up+=1
#         elif i==arr[i]:
#             chk=1
#             if tmp>arr[i]:
#                 up+=1
#             else:
#                 down+=1
#     tmp=arr[i]
#     s=i
# if chk==1:
#     print(max(up,down)-1)
# else:
#     print(min(up,down))

