star = int(input())
star_count = 1
blank = star - 1

for i in range(star):
    star_mark = ' '* blank+'*' * star_count
    star_count = star_count + 1
    blank = blank -1
    print(star_mark)