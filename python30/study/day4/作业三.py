#定义一个重置函数
def chongzhi():
    while True:
        n_money = str(input('请输入充值金额（按q退出重置）:  '))
        if n_money.isnumeric():
            with open(chongzhi) as f:
                f.read()
            print('您已经成功充值%s元,现有账户余额%s元' %(n_money,n_money))
            break
        elif n_money == 'q':
            break
        else:
            print('您输入的重置金额有误，请重新输入')
    return

def gouwuche():
    user_sum = 0
    for i in user_dic.keys():
        u_sum = int(user_dic[i][0]) * user_dic[i][1]
        print("商品名称%s    商品数量%s   金额%s元" %(i,user_dic[i][0],u_sum))
        user_sum = user_sum + u_sum
    print("总金额%s" %user_sum)
    confim = input("输入 “确认” 进行结算\nm  进行充值\nb 返回上一级菜单\nq 退出\n 请输入 :")
    while True:
        if confim == "b" :
            break
        elif confim == "q":
            exit()
        elif confim == 'm':
            chongzhi()
        elif confim == "确认":
            if user_sum >  money :
                print("账户余额不足，请充值后在进行支付，结算金额%s元，账户余额%s元" %(user_sum,money))
                chongzhi()
            else:
                money = money - user_sum
                print("支付成功，您的账户余额%元" %(money))
                break






dic = {'电视':200,'洗衣机':150,'空调':175,'热水器':35,'电脑':500}
user_dic = {}
n_list = {}
print('欢迎光临本商城，祝您此次购物愉快！')
while True:
    print('请输入编号进入相应菜单：\n1、充值\n2、商品列表\n3、进入购物车\n4、返回上一级菜单\n5、退出')
    n = input('')
    #4、返回上一级菜单
    if n == '4' :
        print('已经是首页，请重新输入编号')
        continue
    # 3、购物车
    elif n == '3' :
        gouwuche()
    # 2、商品列表
    elif n == '2' :
        while True:
            i = 1
            for k,v in dic.items():
                print(i,k,v)
                i += 1
            print("输入商品名称购买\ns进入购物车\nb 返回上一级菜单\nq 退出")
            name = input('请输入：  ')
            if name == 'b' :
                break
            elif name == 'q':
                exit()
            elif name == 's':
                gouwuche()
            elif name in dic.keys():
                num = str(input('请输入购买数量：  '))
                if num.isnumeric():
                    if name in user_dic.keys():
                        user_dic[name][0] = int(user_dic[name][0]) + int(num)
                    else:
                        user_dic[name] = [num, dic[name], ]
                else:
                    print('输入的商品数量有误！')
            else:
                print('输入的商品名称有误！')

    #5、退出
    elif n == '5' :
        exit()
    #1、充值
    elif n == '1' :
        chongzhi()
    elif n == '2':
        pass


