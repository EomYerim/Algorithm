import sys

n = int(input())
str=list(map(int,input().split()))
dp=[0]*(n+1)
dp[0]=str[0]
for i in range(n):
    dp[i]=str[0]