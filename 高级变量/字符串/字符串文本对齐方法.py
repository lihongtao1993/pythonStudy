# 定义一个字符串

poem = ["静夜思",
        "李  白",
        "床前明月光",
        "疑是地上霜",
        "举头望明月",
        "低头思故乡"
        ]

for poem_str in poem:
    print("|%s|" % poem_str.center(10, "　"))

