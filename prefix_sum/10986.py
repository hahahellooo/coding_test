import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
s = [0] * n
c = [0] * m # 같은 나머지를 갖는 값이 몇 개있는지 저장
answer = 0

# 합배열 정의하기
s[0] = a[0]
for i in range(1, n):
    s[i] = s[i-1] + a[i]
    
# m을 업데이트 해주기    
for i in range(n):
    remainder = s[i] % m
    if remainder == 0:
        answer += 1
    c[remainder] += 1 # 같은 나머지를 갖는 값이 있을 때마다 +1
    
for i in range(m):
    if c[i] > 1: # 같은 나머지를 갖는 값이 두 개 이상 있으면
        answer += (c[i] * (c[i]-1) //2) # 콤비네이션 계산(s[i] - s[j-1] = 0이면 해당 구간 합이 m으로 나누어 떨어진다는 것을 의미하므로)

print(answer)
