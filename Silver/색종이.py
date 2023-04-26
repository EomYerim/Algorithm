import sys
input=sys.stdin.readline
n=int(input())
arr=[]
w=0
b=0
for i in range(n):
    li=list(map(int,input().split(" ")))
    arr.append(li)
def square(x,y,n):
    global w,b
    square_col=arr[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if arr[i][j]!=square_col:
                square(x,y,n//2)
                square(x,y+n//2,n//2)
                square(x+n//2,y,n//2)
                square(x+n//2,y+n//2,n//2)
                return
    if square_col==0:
        w+=1
    else:
        b+=1

square(0,0,n)
print(w)
print(b)