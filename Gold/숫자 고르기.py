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