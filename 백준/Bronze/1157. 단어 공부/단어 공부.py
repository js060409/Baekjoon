word = input().upper()
setted_word = list(set(word))
count_list = []

for a in setted_word:
    global count
    count = int(word.count(a))
    count_list.append(count)

if count_list.count(max(count_list)) >= 2:
    print('?')
else:
    print(setted_word[(count_list.index(max(count_list)))])