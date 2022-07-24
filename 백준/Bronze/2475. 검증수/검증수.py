first, second, third, fourth, fifth = map(int,input().split())
total = first**2 + second**2 + third**2 + fourth**2 + fifth**2
total2 = total % 10
print(total2)