# 병합 정렬

import sys
input = sys.stdin.readline
result = 0 # 역순 개수를 저장할 변수

n = int(input())
a = list(map(int, input().split()))
tmp = [0] * n # 임시 저장 배열 선언

# s: 시작값, m: 중간값, e: 끝값
def merge_sort(s, e):
	global result
	if s >= e:
        return

    # 중간값 구해서 가장 작은 단위로 나누기
    m = (s + e) // 2 
    merge_sort(s, m)
    merge_sort(m+1, e)

    # 병합(현재 구간을 임시 배열tmp에 저장)
    for i in range(s, e+1):
        tmp[i] = a[i]

    # 병합 결과를 저장할 인덱스
    k = s
    index1 = s
    index2 = m+1
    
    # 병합하면서 역순 개수 계산
    while index1 <= m and index2 <= e:
        if tmp[index1] > tmp[index2]: # 왼쪽 값이 오른쪽 값보다 크면 역순 발생
            a[k] = tmp[index2] # 오른쪽 값(작은 값)을 먼저 배치
            result += index2 - k # 이동 거리만큼 역순 개수 증가 (swap 횟수)
            k += 1
            index2 += 1
        else:
            a[k] = tmp[index1]
            k += 1
            index1 += 1

    # 남은 요소는 인덱스 순서대로 리스트에 추가
    while index1 <= m:
        a[k] = tmp[index1]
        k += 1
        index1 += 1
    while index2 <= e:
        a[k] = tmp[index2]
        k += 1
        index2 += 1

merge_sort(0,n-1)
print(result)





