#!/usr/bin/env python3
LuckNumber = 13
CaiNumber = 1
guess_count = 0
while  guess_count < 3 :
    CaiNumber = input("Please input a number:\t")
    if int( CaiNumber ) > LuckNumber :
        print("the real number is bigger .")
    elif int( CaiNumber ) < LuckNumber :
        print("the real number is smaller .")
    else:
        print("Bingo!")
        break
    guess_count += 1
else:
    print("Too many retrys !")
# if LuckNumber == int( CaiNumber ) :
#     print("Bingo!")
# else:
#     print("Too many retrys !")
