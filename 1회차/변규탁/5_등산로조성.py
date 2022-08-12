import sys
from this import d

sys.stdin = open("_등산로조성.txt")

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(i, j, cut = 0):
    mountain[i][j] = 1
    stack = [(i, j)]
    cnt = 0
    while stack:
        i, j = stack.pop()
        cnt += 1
        for d in range(4):
            nx = i + dx[d]
            ny = j + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if mountain[nx][ny] == 0:
                    if maps[i][j] <= maps[nx][ny]:
                        if maps[i][j] > maps[nx][ny] - K:
                            mountain[nx][ny] = 1
                            dfs(nx,ny,cut)
                            cut += 1
                            stack.append((nx,ny))
                    elif maps[i][j] > maps[nx][ny]:
                        mountain[nx][ny] = 1
                        stack.append((nx, ny))

    return cnt, cut


T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    mountain = [[0]*N for _ in range(N)]

    top = 0
   
    for i in range(N):
        top = max(maps[i])

    max_ = 0
    for i in range(N):
        for j in range(N):
            if maps[i][j] >= top:
                top = maps[i][j]
                cnt, cut = dfs(i,j)
                if cut == 1 :
                    max_ = max(cnt, dfs(i,j)[0]) 
    

    print(f'#{test_case} {max_}')
   
