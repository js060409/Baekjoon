N, X = map(int, input('').split())
A = list(map(int, input().split()))
answer_list =  []

for i in range(len(A)):
    if A[i] < X:
        answer_list.append(A[i])

print(*answer_list)