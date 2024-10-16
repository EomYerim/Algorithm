import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)  # 재귀함수 limit 설정

n = int(input())
# 딕셔너리로 트리 구현
tree = {}
for i in range(n):
    root, left, right = map(str, input().split())  
    tree[root] = left, right 

def preorder(v):  # 전위순회
    if v != ".": # 자식 노드가 있을 경우에만 
        print(v, end="") # 1. 루트
        preorder(tree[v][0])  # 2.  왼쪽 노드 탐색
        preorder(tree[v][1])  # 3.  오른쪽 노드 탐색


def inorder(v):  # 중위순회
    if v != ".": 
        inorder(tree[v][0])  
        print(v, end="")  # 루트 출력
        inorder(tree[v][1])  


def postorder(v):  # 후위순회
    if v != ".": 
        postorder(tree[v][0])  
        postorder(tree[v][1]) 
        print(v, end="")  # 루트 출력

#루트노드 'A'
preorder('A')
print()
inorder('A')
print()
postorder('A')
