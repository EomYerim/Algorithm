from itertools import combinations
import sys
input=sys.stdin.readline
n,s=map(int,input().split(" "))
num_list=list(map(int,input().split(" ")))
def sums():
    res=[]
    cnt=0
    for i in range(1,n+1):
        res.append(list(combinations(num_list,i)))
    for i in range(len(res)):
        for j in range(len(res[i])):
            if sum(res[i][j])==s:
                cnt+=1
    return cnt
print(sums())