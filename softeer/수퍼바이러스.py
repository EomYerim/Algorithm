import sys
input = sys.stdin.readline

K, P, N = map(int, input().split())
mod = 1000000007

# pow(밑, 지수, 모듈러) - 파이썬 내장함수 사용
result = (K * pow(P, 10*N, mod)) % mod
print(result)
