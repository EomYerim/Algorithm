import sys
input = sys.stdin.readline
n,m=map(int,input().split())
students=list(input().rstrip().split())
subject=list(input().rstrip()for _ in range(m))
dic=dict()
for i in subject:
    if i=="-":
        print(n)
    else:
        print(students.count(i))

