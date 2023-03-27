# import sys
# input=sys.stdin.readline
# n=int(input())
# arr=[[i,int(input())] for i in range(1,n+1)]
# for i in range(len(arr)):
#     arr[i] = sorted(arr[i])
# res=[]
# for i in range(len(arr)):
#     if arr[i] in arr[i+1:] or arr[i][0]==arr[i][1]:
       
#         if arr[i][0]==arr[i][1]:
#             res.append(arr[i][0])
#         else:
#             res.append(arr[i][0])
#             res.append(arr[i][1])
# print(len(res))
# for i in sorted(res):
#     print(i)


# import sys
# input=sys.stdin.readline

# n=int(input())

# #res=[[],[1],[2],[3],[4],[5],[6],[7]]
# res=[[],[1],[2],[3],[4],[5],[6]]

# for i in range(1,n+1):
#     x=int(input())
#     res[i].append(x) #1,3 3,1 // 2 1 1 2

#     #res[x].append(i)
#     #res[i].sort()

# print(res)
# arr=sorted(list(set([tuple(set(item)) for item in res])))
# print(arr)

# # print(len(arr))
# # for i in range(1,len(arr)):
# #     for j in arr[i]:
# #         print(j)

def dfs(node,i):
    visited[node]=True
    check=arr[node]
    if not visited[check]:
        dfs(check,i)
    else:
        if visited[check] and check==i:
            res.append(i)
    


n = int(input())	
arr=[0 for _ in range(n+1)]
for i in range(1,n+1):
    arr[i]=int(input())
res =[]	

# dfs 실행
for i in range(1, n+1):
    visited=[False]*(n+1)
    dfs(i,i)

print(len(res))
res.sort()
for i in res:
    print(i)