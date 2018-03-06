lucky_num = 13
input_num = -1
for i in range(3):
    input_num =  int(input("Input the guess num: "))
    if lucky_num > input_num :
        print("the real number is smaller .")
    elif lucky_num < input_num :
        print("the real number is bigger .")
    else:
        print("bingo !")
        break
else :
    print("Too many retrys !")