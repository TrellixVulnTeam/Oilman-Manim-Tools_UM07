from manimlib.imports import*

from workspace.assets.fonts_for_manim import SouseHanSerif


class PrintTexts(Scene):
    def construct(self):
        text = SouseHanSerif("本视频不求三连 觉得有道理随缘给就行\n\n本视频一部分动画采用了Manim（比我想象中的麻烦的多）\n\n感谢你看我发牢骚")
        self.play(Write(text))