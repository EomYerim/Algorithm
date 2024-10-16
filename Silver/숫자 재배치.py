from itertools import permutations
import sys
input=sys.stdin.readline
a,b=map(int,input().split(" "))
res=[]
for j in permutations (str(a),len(str(a))):
    list_a="".join(list(map(str,j)))
    if int(list_a)<=b and int(list_a[0])!=0:
        res.append(list_a)
if len(res)==0:
    print("-1")
else:
    print(max(res))

 
