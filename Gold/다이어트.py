import sys
input= sys.stdin.readline
#G = 현재 몸무게의 제곱에서 성원이가 기억하고 있던 몸무게의 제곱을 뺀 것
G=int(input())
#가능한 성원이의 현재 몸무게를 오름차순으로 출력, 가능한 몸무게가 없다면 -1
#g=c**2 - r**2 = 15
res=[]
for i in range(1,G+1):
    j=G//i
    if G%i==0 and j<i and (i+j)%2==0:
            x=(i+j)//2 
            res.append(x)
if len(res)==0:
    print(-1)
else:
    for i in sorted(res):
        print(i)


