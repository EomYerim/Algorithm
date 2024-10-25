# import sys
# P,N = map(int,input().split())
# virus = list(map(int,input().split()))
# sum=0
# for i in virus:
#     sum+=(i*P)
# print(sum%1000000007)

import sys
input = sys.stdin.readline
P,N = map(int,input().split())
virus = list(map(int,input().split()))
P_powers=[1]*(N+1)
mod=1000000007
sum=0
for i in range(1,N+1):
    P_powers[i]=(P_powers[i-1]*P)%mod

for i in range(N):
    if i == N - 1:
        sum += virus[i] % mod
    else:
        sum += (virus[i] * P_powers[N - 1 - i]) % mod

sum %= mod
print(sum)
