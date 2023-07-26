org_nums = []

for i in range(10):
    a = int(input())
    org_nums.append(a)

divided_nums = []
for i in range(len(org_nums)):
    a = int(org_nums[i] % 42)
    divided_nums.append((a))

print(len(list(set(divided_nums))))