import sys

sys.stdin = open("_모음이보이지않는사람.txt")



T = int(input())

for test_case in range(1, T + 1):
    word = input()
    answer = word
    for char in word:
        if char in 'aeiou':
            answer = answer.replace(char, '')

    print(f'#{test_case} {answer}')