import sys

sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    card = list(input().split())
    shuffle = []
    if N % 2 == 1:
        idx = (N+1)//2
        for i in range(idx-1):
            shuffle.append(card[:idx][i]) 
            shuffle.append(card[idx:][i])
        shuffle.append(card[idx-1])    
    else:
        idx = N // 2
        for i in range(idx):
            shuffle.append(card[:idx][i]) 
            shuffle.append(card[idx:][i])

    print('#{} {}'.format(test_case, ' '.join(shuffle)))  


