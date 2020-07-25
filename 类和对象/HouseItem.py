class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s]占地%.2f" % (self.name, self.area)


class House:
    def __init__(self, house_Type, area):
        self.house_Type = house_Type
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具列表
        self.item_list = []

    def __str__(self):
        return ("户型：%s\n总面积：%.2f\n剩余面积：%.2f\n家具：%s" %
                (self.house_Type, self.area, self.free_area, self.item_list))

    def add_item(self, item):
        print("要添加%s" % item)
        # 判断剩余面积
        if item.area > self.free_area:
            print("不能添加！")
            return

        # 添加家具
        self.item_list.append(item.name)

        # 计算剩余面积
        self.free_area = self.free_area - item.area


# 创建家具

bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("桌子", 1.5)

print(bed)
print(chest)
print(table)


# 创建家
house = House("两室一厅", 75)

house.add_item(bed)
house.add_item(chest)
house.add_item(table)
print(house)
