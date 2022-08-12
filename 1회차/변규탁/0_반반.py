import sys

sys.stdin = open("_반반.txt")

T = int(input())


for test_case in range(1, T + 1):
    words = dict()
    valid = True
    S = input()
    for word in S:
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1

    for v in words.values():
        if v != 2:
            valid = False 
    
    if len(words) == 2 and valid:
        print(f'#{test_case} Yes')
    else:
        print(f'#{test_case} No')