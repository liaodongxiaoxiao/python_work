from random import choice


class RandomWork():
    """一个生成随机漫步数据类"""

    def __init__(self, number_points=5000):
        """初始化随机漫步的属性"""
        self.number_points = number_points

        # 所有漫步始于原点
        self.x_value = [0]
        self.y_value = [0]

    def fill_walk(self):
        """计算随机漫步所有点"""

        while len(self.x_value) < self.number_points:
            # 沿x移动的方向，-1← 1→
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            # 沿y轴移动
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # 原点重新计算
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x和y
            next_x = self.x_value[-1] + x_step
            next_y = self.y_value[-1] + y_step

            self.x_value.append(next_x)
            self.y_value.append(next_y)
