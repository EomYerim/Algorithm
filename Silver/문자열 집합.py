import sys
input=sys.stdin.readline
n,m=map(int,input().split(" "))

dic=dict()
str_li=dict()
cnt=0
for i in range(n):
    dic[i]=str(input()).rstrip()
for i in range(m):
    str_li[i]=str(input()).rstrip()

for i in str_li.values():
    if i in dic.values():
        cnt+=1

print(cnt)