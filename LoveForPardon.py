import random
import math
import tkinter as tk
from tkinter import Canvas, Tk

CANVAS_WIDTH: int = 640
CANVAS_HEIGHT: int = 480
CANVAS_CENTER_X: int = CANVAS_WIDTH // 2
CANVAS_CENTER_Y: int = CANVAS_HEIGHT // 2
IMAGE_ENLARGE_RATIO: int = 11
HEART_COLOR: str = "#ff2190"
HEART_POINT_COUNT: int = 2000
EDGE_SCATTER_COUNT: int = 3
SCATTER_BETA: float = 0.15
BEAT_FORCE_RATIO: float = 11.6
ANIMATION_INTERVAL_MS: int = 160
POINT_SIZE_MIN: int = 1
POINT_SIZE_MAX: int = 3


class Heart:
    """
    心形图案生成与渲染类。

    通过数学公式生成心形曲线上的坐标点，并使用内部散射算法
    生成边缘扩展点，最终渲染带有跳动效果的爱心动画。

    Attributes:
        original_heart_coordinates: 心形原始轮廓坐标点集合
        edge_expansion_coordinates: 心形边缘扩展散射坐标点集合
    """

    def __init__(self) -> None:
        self.original_heart_coordinates: set[tuple[int, int]] = set()
        self.edge_expansion_coordinates: set[tuple[int, int]] = set()

    def heart_function(self, t: float, shrink_ratio: int = IMAGE_ENLARGE_RATIO) -> tuple[int, int]:
        """
        心形参数方程，根据参数 t 计算心形曲线上的坐标点。

        使用经典的心形参数方程公式：
        x = 16 * sin(t)^3
        y = -(13 * cos(t) - 5 * cos(2t) - 2 * cos(3t) - cos(4t))

        Args:
            t: 参数角度，范围 [0, 2π]
            shrink_ratio: 缩放比例，用于控制心形大小

        Returns:
            转换到画布坐标系后的 (x, y) 整数坐标元组
        """
        x: float = 16 * (math.sin(t) ** 3)
        y: float = -(13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t))
        return (
            int(x * shrink_ratio + CANVAS_CENTER_X),
            int(y * shrink_ratio + CANVAS_CENTER_Y),
        )

    def scatter_inside(self, x: int, y: int, beta: float = SCATTER_BETA) -> tuple[int, int]:
        """
        在心形内部随机散射一个点，用于生成边缘扩展效果。

        使用指数分布生成随机散射比例，使得散射点更集中于原始点附近，
        同时也有一定概率散射到较远位置，形成自然的光晕效果。

        Args:
            x: 原始参考点的 x 坐标
            y: 原始参考点的 y 坐标
            beta: 散射强度参数，值越大散射范围越广

        Returns:
            散射后的 (x, y) 整数坐标元组
        """
        ratio_x: float = -beta * math.log(random.random())
        ratio_y: float = -beta * math.log(random.random())
        x0, y0 = self.heart_function(t=random.uniform(0, 2 * math.pi))
        return (
            int((x0 + (x - x0) * ratio_x)),
            int((y0 + (y - y0) * ratio_y)),
        )

    def build(self, number: int = HEART_POINT_COUNT) -> None:
        """
        构建心形坐标集合。

        生成指定数量的原始心形轮廓点，并为每个轮廓点生成
        多个边缘扩展散射点。每个边缘扩展点都基于原始轮廓点
        进行独立散射，确保散射分布均匀。

        Args:
            number: 心形原始轮廓点的数量，默认值为 HEART_POINT_COUNT
        """
        for _ in range(number):
            t: float = random.uniform(0, 2 * math.pi)
            x_original, y_original = self.heart_function(t)
            self.original_heart_coordinates.add((x_original, y_original))
            for _ in range(EDGE_SCATTER_COUNT):
                x_scatter, y_scatter = self.scatter_inside(x_original, y_original)
                self.edge_expansion_coordinates.add((x_scatter, y_scatter))

    @staticmethod
    def calc_position(x: int, y: int, ratio: float) -> tuple[float, float]:
        """
        计算心形跳动动画中的坐标偏移。

        基于与画布中心距离的平方反比力模型，模拟心跳收缩效果。
        距离中心越近的点受到的力越大，收缩效果越明显，形成自然的跳动视觉。

        Args:
            x: 原始 x 坐标
            y: 原始 y 坐标
            ratio: 力的比例系数，控制跳动幅度

        Returns:
            跳动偏移后的 (x, y) 浮点坐标元组
        """
        force: float = 1 / ((x - CANVAS_CENTER_X) ** 2 + (y - CANVAS_CENTER_Y) ** 2) ** 0.6
        dx: float = ratio * force * (x - CANVAS_CENTER_X)
        dy: float = ratio * force * (y - CANVAS_CENTER_Y)
        return x - dx, y - dy

    @staticmethod
    def calc_position_static(x: int, y: int, ratio: float) -> tuple[float, float]:
        """
        calc_position 的静态方法别名。

        提供与实例无关的统一调用接口，确保在静态上下文中也能
        正确计算跳动坐标。

        Args:
            x: 原始 x 坐标
            y: 原始 y 坐标
            ratio: 力的比例系数，控制跳动幅度

        Returns:
            跳动偏移后的 (x, y) 浮点坐标元组
        """
        return Heart.calc_position(x, y, ratio)

    def render(self, render_canvas: Canvas, render_frame: int) -> None:
        """
        在画布上渲染心形图案（单帧）。

        依次渲染边缘扩展点和原始轮廓点，边缘扩展点形成外围光晕，
        原始轮廓点构成心形主体，两者叠加产生饱满的视觉效果。
        每个点的大小随机，增加画面的层次感。

        Args:
            render_canvas: Tkinter Canvas 画布对象
            render_frame: 当前帧编号（预留用于帧间差异化效果）
        """
        render_canvas.delete("all")
        for x, y in self.edge_expansion_coordinates:
            x, y = self.calc_position_static(x, y, BEAT_FORCE_RATIO)
            size: int = random.randint(POINT_SIZE_MIN, POINT_SIZE_MAX)
            render_canvas.create_rectangle(x, y, x + size, y + size, width=0, fill=HEART_COLOR)
        for x, y in self.original_heart_coordinates:
            x, y = self.calc_position_static(x, y, BEAT_FORCE_RATIO)
            size = random.randint(POINT_SIZE_MIN, POINT_SIZE_MAX)
            render_canvas.create_rectangle(x, y, x + size, y + size, width=0, fill=HEART_COLOR)


class HeartInterface:
    """
    心形动画界面管理类。

    负责创建 Heart 实例、构建坐标数据，并驱动 Tkinter 动画循环。
    作为 Heart 类与 Tkinter 主循环之间的协调层。

    Attributes:
        heart_instance: 心形图案生成器实例
    """

    def __init__(self) -> None:
        self.heart_instance: Heart = Heart()
        self.heart_instance.build()

    def draw(self, main: Tk, render_canvas: Canvas, render_frame: int) -> None:
        """
        动画绘制循环回调函数。

        调用 Heart.render() 绘制当前帧，并通过 main.after()
        调度下一帧的绘制，形成连续的动画效果。

        Args:
            main: Tkinter 主窗口 (Tk) 对象
            render_canvas: 用于绘制的 Canvas 画布对象
            render_frame: 当前帧编号
        """
        render_canvas.delete("all")
        self.heart_instance.render(render_canvas, render_frame)
        main.after(ANIMATION_INTERVAL_MS, self.draw, main, render_canvas, render_frame + 1)


def main() -> None:
    """
    程序主入口函数。

    初始化 Tkinter 环境，创建主窗口和画布，
    启动心形动画并进入主事件循环。
    """
    root: Tk = tk.Tk()
    canvas: Canvas = tk.Canvas(root, bg="black", height=CANVAS_HEIGHT, width=CANVAS_WIDTH)
    canvas.pack()
    heart_interface_instance: HeartInterface = HeartInterface()
    heart_interface_instance.draw(root, canvas, 0)
    root.mainloop()


if __name__ == "__main__":
    main()
