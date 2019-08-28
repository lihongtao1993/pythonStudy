 # 定义玩家和电脑出拳值
player = int(input("请出拳，1：石头，2剪刀，3：布"))
computer = 1
 # 判断胜负
if (
    (player == 1 and computer == 2)
        or(player == 2 and computer == 3)
        or(player == 3 and computer == 1)):
        print("你赢了！！！！！！！！")
elif player == computer:
    print("平局")
else:
    print("你输了")
