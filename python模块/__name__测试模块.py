def demo():
    print("测试__name__")


# 在开发模块是增加__name__的判断，不需要再导入时执行的代码，就不会执行了
if __name__ == "__main__":
    # 直接执行模块文件，__name__的结果永远都是是__main__
    print(__name__)


    print("没有缩进的代码导入时都会被执行一遍")
    demo()
