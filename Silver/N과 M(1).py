from itertools import permutations
n,m=map(int,input().split())
if m==1:
    list=[print(i) for i in range(1,n+1)]
else:
    arr=[i for i in range(1,n+1)]
    for i in permutations(arr,m):
        print(*i)
