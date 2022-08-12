import sys

sys.stdin = open("_창용마을무리의개수.txt")


T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    town = [[] for _ in range(N+1)]
    
    for _ in range(M):
        v1, v2 = map(int, input().split())
        town[v1].append(v2)
        town[v2].append(v1)

    cnt = 0
    people = []
    for i in range(1, N + 1):
        if i not in people:
            stack = [i]
            while stack:
                v = stack.pop()
                if v not in people:
                    people.append(v)
                    for w in town[v]:
                        stack.append(w)
            cnt += 1
    print(f'#{test_case} {cnt}')