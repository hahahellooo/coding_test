import sys

n = int(input())
ans = [0]*n # n의 길이만큼 리스트 초기화
a = list(map(int, input().split()))
mystack = []

for i in range(n):
    while mystack and a[mystack[-1]] < a[i]: # 스택에서 마지막 숫자를 확인
        ans[mystack.pop()] = a[i] # 시간 복잡도를 줄이기 위해 크기 비교가 끝난 숫자는 pop
    mystack.append(i)

while mystack:
    ans[mystack.pop()] = -1

for i in range(n):
    sys.stdout.write(str(ans[i]) + " ")
