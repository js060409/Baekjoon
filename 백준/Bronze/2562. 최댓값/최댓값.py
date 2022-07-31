list = []

for i in range(9):
    list.append(int(input()))

print(max(list))

for i in range(9):
    if list[i] == max(list):
        print(i + 1)