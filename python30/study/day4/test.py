

while True:
    n_money = str(input('请输入充值金额（按q退出重置）:  '))
    if n_money.isnumeric():
        f = open('chongzhi', 'w')
        f.write(n_money)
        f.close()
        f = open('chongzhi', 'r')
        for line in f:
            print(line)

        print('您已经成功充值%s元,现有账户余额%s元' % (n_money, n_money))
        break
    elif n_money == 'q':
        break
    else:
        print('您输入的重置金额有误，请重新输入')
