# loveForpardon

## 打火机与公主裙

- 改编自 Twentine 同名小说，讲述独立勇敢乖乖女与霸道天才学霸相互吸引、走近、共同成长的故事。
- 本仓库收录剧中出现的「爱心代码」。

## 文件说明

| 文件 | 说明 |
| --- | --- |
| `LoveForPardon.py` | tkinter 版爱心动画，基于心形参数方程 + 跳动效果 |
| `B-loveForpardon` | turtle 版爱心绘制与闪烁动画 |

## 依赖说明（零第三方库）

两个脚本**只使用 Python 标准库**，无需 `pip install` 任何东西。

| 标准库 | 在项目中做的事 | 为什么这样选 |
|---|---|---|
| `tkinter` | `LoveForPardon.py` 的 Canvas 逐帧刷新：心形参数方程采样 + 随机扩散点 + 跳动缩放 | 标准库自带 GUI，零依赖、双击即跑；逐帧重绘比引入游戏引擎轻得多 |
| `turtle` | `B-loveForpardon` 的笔触绘制与闪烁动画 | 用最少代码画出平滑曲线，适合演示型小动画 |
| `math` / `random` | 心形曲线计算、扩散点抖动、跳动幅度与颜色随机 | 标准库，无需 NumPy 这类重量级依赖 |

## 运行方式

```bash
# tkinter 版
python LoveForPardon.py

# turtle 版
python B-loveForpardon
```

> 依赖 Python 3，`tkinter` 与 `turtle` 均为标准库，无需额外安装。

### 特别感谢

[<img src="https://user-images.githubusercontent.com/11474360/112592917-baa00600-8e41-11eb-9da4-ecb53bb3c2fa.png" width="200"/>](https://jb.gg/OpenSource)

## 鸣谢（Acknowledgments）

感谢以下原作者与工具（图标均取自官方站点 / CDN）：

<table>
  <tr>
    <td align="center" width="140">
      <a href="https://www.python.org/">
        <img src="https://www.python.org/static/img/python-logo.png" width="64" height="64" alt="Python" /><br />
        <sub><b>Python</b></sub>
      </a>
      <br />
      <sub>tkinter / turtle 标准库</sub>
    </td>
    <td align="center" width="140">
      <a href="https://www.jetbrains.com/idea/">
        <img src="https://resources.jetbrains.com/storage/products/intellij-idea/img/meta/intellij-idea_logo_300x300.png" width="64" height="64" alt="IntelliJ IDEA" /><br />
        <sub><b>IntelliJ IDEA</b></sub>
      </a>
      <br />
      <sub>JetBrains 出品</sub>
    </td>
    <td align="center" width="140">
      <a href="https://www.jetbrains.com/pycharm/">
        <img src="https://resources.jetbrains.com/storage/products/pycharm/img/meta/pycharm_logo_300x300.png" width="64" height="64" alt="PyCharm" /><br />
        <sub><b>PyCharm</b></sub>
      </a>
      <br />
      <sub>JetBrains 出品</sub>
    </td>
  </tr>
</table>

| 项目 / 人物 | 贡献 | 说明 |
|---|---|---|
| Twentine（量小公子） | 小说《打火机与公主裙》原著作者，本仓库剧集内容之来源 | 著作权归原作者，本仓库仅收录剧中「爱心代码」，不作商业用途 |
| [Python](https://www.python.org/)（`tkinter` / `turtle`） | 全部绘图与动画能力 | PSF License |
| [JetBrains](https://www.jetbrains.com/) | 提供 IntelliJ IDEA / PyCharm 等开发工具 | 商业授权（开源项目可申请免费许可证） |

> 爱心代码的具体源流：_（待补充，若改编自某位作者的公开实现，请在此署名并附链接）_
> 贡献者名单：_（待补充，欢迎在 PR 中署名）_

## 提交统计

<div align="center"> <img src="https://github-readme-stats.vercel.app/api?username=leipengic&show_icons=true&theme=tokyonight" /> </div>

## 语言统计

<div align="center"> <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=leipengic" /> </div>

## 打卡统计

<div align="center"> <img src="https://github-readme-streak-stats.herokuapp.com/?user=leipengic" /> </div>
