list_one = ["1、北京","2、河北"]
beijing_list = ["1、朝阳区","2、海淀区"]
hebei_list = ["1、承德","2、廊坊"]
chaoyang_list = ["1、双井","2、国贸"]
haidian_list = ["1、中关村","2、海淀黄庄"]
chengde_list = ["1、双滦区","2、双桥区"]
langfang_list = ["1、大厂","2、燕郊"]
while True:
    print("请输入编号进入相应菜单\n输入'b'返回上一次菜单\n输入'q'退出程序\n")
    for line in list_one:
        print(line)
    input_num = input("请输入选项：")
    if input_num == 'b':
        continue
    elif input_num == 'q':
        break
    elif input_num == "1":
        while True:
            print("请输入编号进入相应菜单\n输入'b'返回上一次菜单\n输入'q'退出程序\n")
            for line in beijing_list:
                print(line)
            input_num = input("请输入选项：")
            if input_num == 'b':
                break
            elif input_num == 'q':
                exit()
            elif input_num == '1':
                while True:
                    print("请输入'b'返回上一次菜单\n输入'q'退出程序\n")
                    for line in chaoyang_list:
                        print(line)
                    input_num = input("请输入选项：")
                    if input_num == 'b':
                        break
                    elif input_num == 'q':
                        exit()
                    else:
                        print("输入错误请重新输入,请重新输入")

            elif input_num == '2':
                while True:
                    print("请输入'b'返回上一次菜单\n输入'q'退出程序\n")
                    for line in haidian_list:
                        print(line)
                    input_num = input("请输入选项：")
                    if input_num == 'b':
                        break
                    elif input_num == 'q':
                        exit()
                    else:
                        print("输入错误请重新输入,请重新输入")

    elif input_num == "2":
        while True:
            print("请输入编号进入相应菜单\n输入'b'返回上一次菜单\n输入'q'退出程序\n")
            for line in hebei_list:
                print(line)
            input_num = input("请输入选项：")
            if input_num == 'b':
                break
            elif input_num == 'q':
                exit()
            elif input_num == '1':
                while True:
                    print("请输入'b'返回上一次菜单\n输入'q'退出程序\n")
                    for line in chengde_list:
                        print(line)
                    input_num = input("请输入选项：")
                    if input_num == 'b':
                        break
                    elif input_num == 'q':
                        exit()
                    else:
                        print("输入错误请重新输入,请重新输入")
            elif input_num == '2':
                while True:
                    print("请输入'b'返回上一次菜单\n输入'q'退出程序\n")
                    for line in langfang_list:
                        print(line)
                    input_num = input("请输入选项：")
                    if input_num == 'b':
                        break
                    elif input_num == 'q':
                        exit()
                    else:
                        print("输入错误请重新输入,请重新输入")
    else:
        print("输入错误请重新输入,请重新输入")

