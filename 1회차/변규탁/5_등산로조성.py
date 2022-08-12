import sys

sys.stdin = open("_등산로조성.txt")

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(i, j, cnt, cut):
    global answer
    mountain[i][j] = 1
    for d in range(4):
        nx = i + dx[d]
        ny = j + dy[d]
        if 0 <= nx < N and 0 <= ny < N:
            if mountain[nx][ny] == 0:
                if maps[i][j] > maps[nx][ny]:
                    mountain[nx][ny] = 1
                    dfs(nx, ny, cnt+1, cut)
                    mountain[nx][ny] = 0
                if cut == 0 and maps[nx][ny] >= maps[i][j] and maps[nx][ny] - maps[i][j] + 1 <= K:
                    mountain[nx][ny] = 1
                    height = maps[nx][ny]
                    maps[nx][ny] = maps[nx][ny] - (maps[nx][ny]-maps[i][j] +1)
                    dfs(nx, ny, cnt+1, 1)
                    mountain[nx][ny] = 0
                    maps[nx][ny] = height

    answer = max(answer, cnt)
    mountain[i][j] = 0

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    mountain = [[0]*N for _ in range(N)]

    top = 0
    for i in range(N):
        for j in range(N):
            if maps[i][j] > top:
                top = maps[i][j]
    answer = 0
    for i in range(N):
        for j in range(N):
            if maps[i][j] == top:
                dfs(i,j,1,0)
    
    print(f'#{test_case} {answer}')