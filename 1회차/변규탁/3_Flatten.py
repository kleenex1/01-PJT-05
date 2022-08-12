import sys

sys.stdin = open("_Flatten.txt")


for test_case in range(1,10+1):
    dump = int(input())
    list_ = list(map(int, input().split()))
    
    for _ in range(dump):
        max_ = 0
        max_idx = 0
        min_ = 1000
        min_idx = 0
        for i in range(len(list_)):
            if list_[i] > max_:
                max_ = list_[i]
                max_idx = i
        for i in range(len(list_)):
            if list_[i] < min_:
                min_ = list_[i]
                min_idx = i

        list_[max_idx] -= 1
        list_[min_idx] += 1

    print(f'#{test_case} {max(list_) - min(list_)}')

    