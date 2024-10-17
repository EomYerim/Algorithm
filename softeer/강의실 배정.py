import sys

N=int(input())
lecture=[]

for _ in range(N):
    a,b=map(int,input().split())
    lecture.append([a,b])

sort_lecture = sorted(lecture, key=lambda x: x[1])
target=sort_lecture[0][1] 
cnt=1
for i in sort_lecture:
    if i[0]>=target:
        target=i[1]
        cnt+=1
print(cnt)
