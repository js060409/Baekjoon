n = int(input())

for i in range(n):
    num, s = input().split()
    num = int(num)
    answer = ''

    for o in (s):
        answer += o * num
    print(answer)