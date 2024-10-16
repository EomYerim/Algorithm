import sys
input = sys.stdin.readline
k,s,n=map(str,input().split(" "))
move=[input().rstrip()for i in range(int(n))]
dic=dict()
alphaDic=dict()
alpha=['A','B','C','D','E','F','G','H']
for i in range(8):
    alphaDic[alpha[i]]=i+1

for i in move:
    if i=="R":
        dic[i]=(1,0)
    if i=="L":
        dic[i]=(-1,0)
    if i=="B":
        dic[i]=(0,-1)
    if i=="T":
        dic[i]=(0,1)
    if i=="RT":
        dic[i]=(1,1)
    if i=="LT":
        dic[i]=(-1,1)
    if i=="RB":
        dic[i]=(1,-1)
    if i=="LB":
        dic[i]=(-1,-1)
x=alphaDic[k[0]]
y=int(k[1])
sx=alphaDic[s[0]]
sy=int(s[1])
for i in move:
    dx, dy = dic[i]
    tempX, tempY = x + dx, y + dy
    if 1 <= tempX <= 8 and 1 <= tempY <= 8:
        if (tempX, tempY) == (sx, sy):
            tempSX, tempSY = sx + dx, sy + dy
            if 1 <= tempSX <= 8 and 1 <= tempSY <= 8:
                sx, sy = tempSX, tempSY
                x, y = tempX, tempY
        else:
            x, y = tempX, tempY

resDic=dict(map(reversed, alphaDic.items()))
print(str(resDic[x])+str(y))
print(str(resDic[sx]+str(sy)))