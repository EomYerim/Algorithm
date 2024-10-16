from math import ceil
n,c,w=map(int,input().split())
tree=[int(input()) for _ in range(n)]
res=[]
for i in range(1,max(tree)+1):
    trees=[]
    for j in tree:
        x=j//i
        trees.append(max(0,x*i*w - (ceil(j/i)-1)*c))
    res.append(sum(trees))
print(max(res))



