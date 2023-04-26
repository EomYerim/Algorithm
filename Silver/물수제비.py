import sys
input=sys.stdin.readline
n=int(input())
arr=[0]+list(map(int,input().split(" ")))
d=[]
d.append([1,sum(arr)])
for i in range(2,n+1):
    res=0
    for j in range(i,n+1,i):
        res+=arr[j]
    d.append([i,res])
c=sorted(d,key=lambda x:-x[1])
if c[0][1]<=0:
    c[0]=[0,0]
print(*c[0])