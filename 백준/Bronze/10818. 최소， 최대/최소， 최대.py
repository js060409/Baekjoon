a = int(input())
list_one = []

list_one.append(list(map(int, input().split())))

print((min(list_one[0])), max(list_one[0]))