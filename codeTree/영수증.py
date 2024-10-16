import sys
input = sys.stdin.readline
n=int(input()) # 처음 금액 입력 받기
k=int(input())
res=0
for i in range(k):
    a,b=map(int,input().split(" "))
    res+=a*b
print("Yes") if res==n else print("No")

