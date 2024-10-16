from itertools import combinations
import sys
input=sys.stdin.readline
n=int(input())
s=[i for i in range(0,10)]
arr=[]
if n<=10:
    print(n)
else:
    for i in range(1,11):
        for j in combinations(s,i):
            tmp=list(j)
            tmp.sort(reverse=True)
            arr.append("".join(str(i) for i in tmp))
    c=sorted(int(i) for i in arr)
    if len(c)<=n:
        print(-1)
    else:
        print(c[n])


