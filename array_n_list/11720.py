n = int(input())
numlist = str(input()) # 여기서 처음부터 리스트로 만들었으면 for문에서 list 사용하지 않아도 됐을텐데..
result = 0

for i in list(numlist):
    result+=int(i)

print(result)
