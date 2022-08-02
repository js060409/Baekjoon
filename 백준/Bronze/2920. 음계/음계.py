A,B,C,D,E,F,G,H = map(int,input().split())

if [A,B,C,D,E,F,G,H] == [1,2,3,4,5,6,7,8]:
    print('ascending')
    
elif [A,B,C,D,E,F,G,H] == [8,7,6,5,4,3,2,1]:
    print('descending')

else:
    print('mixed')