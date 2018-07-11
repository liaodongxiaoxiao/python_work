class GameStats:
    """统计游戏状态"""

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.game_active = False
        self.high_score = 0
        # self.ship_left = self.ai_settings.ship_limit
        self.reset_stats()

    def reset_stats(self):
        """初始化统计用的参数"""
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
