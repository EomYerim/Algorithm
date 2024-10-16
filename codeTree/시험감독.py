import sys
#n : 시험장 개수
#a : 시험장 응시자 수 
#b,c : 각 감독이 응시할 수 있는 응시자 수
input=sys.stdin.readline

n=int(input())
a = list(map(int, input().split()))
b,c=map(int,input().split())
li = [i - b for i in a if i > b]
cnt=0
for i in li:
    if i<=c:
        cnt+=1
    else:
        if(i%c==0):
            cnt+=i//c
        else:
            cnt+=i//c
            cnt+=1
print(cnt+n)