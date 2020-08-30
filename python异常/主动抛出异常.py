# 主动抛出异常的步骤：
# 1、创建异常，Exceptionl类创建一个异常对象
# 2、抛出异常


def input_password():
    password = input("请输入密码：")
    if len(password) >= 8:
        return password
    # 密码长度不符，主动抛出异常
    # 1、创建一个异常对象
    ex = Exception("长度小于8")
    # 抛出异常，使用raise语法
    raise ex


try:
    input_password()
except Exception as result:
    print('错误信息：%s' % result)
