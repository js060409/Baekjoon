suuuuu = int(input())
ox = []
score = 0
bonus = 1


for i in range(suuuuu):
    ox = list(input())
    for j in range(len(ox)):
        if ox[j] == "O":
            score = score +bonus
            bonus = bonus+ 1
            
        else:
            bonus = 1
    print(score)
    score = 0
    bonus = 1