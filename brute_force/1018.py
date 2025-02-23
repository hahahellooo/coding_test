# 백준 1018 체스판 다시 칠하기

n,m = map(int, input().split())
board = [input() for _ in range(n)]

count = []
for a in range(n-7):
    for b in range(m-7):
        w_index = 0 # w로 시작할 때 잘못 칠한 칸의 개수
        b_index = 0 # b로 시작할 때 잘못 칠한 칸의 개수
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if board[i][j] != 'W':
                        w_index += 1
                    else:
                        b_index += 1
                else:
                    if board[i][j] != 'W':
                        b_index += 1
                    else:
                        w_index += 1
        count.append(w_index)
        count.append(b_index)

print(min(count))


