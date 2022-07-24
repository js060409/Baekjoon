A = int(input()) 
B = input()
C = 0

number = list(B)
for i in range(A):
    C = C + int(number[i])
print(C)