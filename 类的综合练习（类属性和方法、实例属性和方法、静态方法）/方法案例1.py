class Game:
    top_score = 0

    def __init__(self,playerName):
        self.playName = playerName

    @staticmethod
    def show_help():
        print("帮助信息……")

    @classmethod
    def show_topScore(cls):
        print("历史最高分是%d" % cls.top_score)

    def start_game(self):
        print("%s开始玩游戏……" % self.playName)

Game.show_help()

Game.show_topScore()

xiaoming = Game("小明")

xiaoming.start_game()