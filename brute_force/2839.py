# 백준 2839 설탕 배달

# 그리디 
n = int(input())
count = 0

while n >= 0:
    if n%5 == 0:
        count += n//5
        print(count)
        break # n이 5로 나누어 덜어져도 n >= 0 조건을 만족하기 때문에 break 필수
    n -= 3
    count+=1
else:
    print(-1)


# 브루트 포스
n = int(input())

for i in range(n//5, -1, -1):
    remain = n - (5 * i)
    if remain % 3 == 0:
        print(i + remain // 3)
        break
else:
    print(-1)


# 동적 계획법(DP)
n = int(input())

dp = [-1] * n+1 # pd[i] = i kg으로 만들 수 있는 최소 봉지 수  
if n >= 3:
    dp[3] = 1
if n >= 5:
    dp[5] = 1

for i in range(6, n+1):
    if dp[i-3] != -1:
        dp[i] = dp[i-3] + 1
    # 5의 배수라서 봉지 갯수를 +1 하지만 이미 카운트 되어 있는 숫자에 봉지 갯수를 +1하는 것과
    # 기존의 봉지 갯수 중 더 작은 수를 반환
    if dp[i-5] != -1:
        dp[i] = min(dp[i], dp[i-5] + 1) if dp[i] != -1 else dp[i-5] + 1


print(dp[n])



        
