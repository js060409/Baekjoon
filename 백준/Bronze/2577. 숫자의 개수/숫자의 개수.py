A = int(input())
B = int(input())
C = int(input())

cal_answer = str(A * B * C)
listed_cal = list(cal_answer)

zero = 0
one = 0
two = 0
three =0 
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0

for i in range(len(listed_cal)):
    if listed_cal[i] == '0' :
        zero = zero + 1
    
    elif listed_cal[i] =='1' :
        one = one + 1

    elif listed_cal[i] == '2' :
        two = two + 1

    elif listed_cal[i] == '3':
        three = three + 1
    
    elif listed_cal[i] == '4':
        four = four + 1

    elif listed_cal[i] == '5':
        five = five + 1

    elif listed_cal[i] == '6':
        six = six + 1

    elif listed_cal[i] == '7':
        seven = seven + 1
    
    elif listed_cal[i] == '8':
        eight = eight + 1

    elif listed_cal[i] == '9':
        nine = nine + 1

print(zero)
print(one )
print(two )
print(three )
print(four )
print(five )
print(six )
print(seven) 
print(eight)
print(nine)