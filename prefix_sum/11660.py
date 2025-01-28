import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = [[0] * (n+1)] # n+1의 길이로 초기화
d = [[0]*(n+1) for _ in range(n+1)] # (n+1) * (n+1) 로 초기화

# 초기 배열생성
for i in range(n):
    a_row = [0] + [int(x) for x in input().split()]
    a.append(a_row)

# 합 배열 생성
for i in range(1, n+1):
    for j in range(1, n+1):
        d[i][j] = d[i][j-1] + d[i-1][j] -d[i-1][j-1] + a[i][j]

# m 번만큼 연        
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = d[x2][y2] -d[x1-1][y2] -d[x2][y1-1] + d[x1-1][y1-1]
    print(result)
