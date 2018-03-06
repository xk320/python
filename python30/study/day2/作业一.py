#用户输入用户名
username = input("Please input your username: ")
#判断用户名是否被系统锁定,用户名是否存在
f_lock = open("锁定用户", "r")
f_user = open("用户文件", "r")
if username in f_lock.read():
    print("您的用户已经被锁定！")
else:
#进行用户名密码效验，多少输入三次密码，三次错误用户名将被系统锁定
    for i in range(3):
        print(i)
        userpass = input("Please input your password: ")
        userlist = username + " " + userpass
        f = open("用户文件", "r")
        if userlist in f.read():
            print("welcome to system!")
            f.close()
            break
        else:
            if i == 2 :
                continue
            else:
                print("用户名或密码错误请重试\n")
                f.close()
    else:
        f_lock.close()
        f_lock = open("锁定用户", "a")
        f_lock.write(username+"\n")
        print("三次密码错误，您的用户被锁定！")
f_lock.close()

