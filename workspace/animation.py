import os
import sys
# from manim.manimlib.imports import *
from manimlib.imports import *

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
# ######################################## For bat
from workspace.a_lot_of_assets.fonts_for_manim import SouseHanSerifText


class TempClass(Scene):
    def construct(self):
        text = SouseHanSerifText(
            "论证完毕",
            color=BLUE
        ).scale(3)
        text2 = SouseHanSerifText(
            "QED",
            color=RED
        ).scale(3)
        self.play(Write(text))
        self.wait(1)
        self.play(Transform(text, text2))


class svg(Scene):
    def construct(self):
        text1 = SouseHanSerifText(
            "数字论证",
            t2c={"论证": BLUE}
        ).scale(2)
        four = SouseHanSerifText(
            "4",
            color=BLUE
        ).scale(2)

        AIPC = SouseHanSerifText(
            "AIPC",
            t2c={"MacBook": YELLOW,
                 "AIPC": RED,
                 "先进": BLUE}
        ).scale(2)
        applePC = SouseHanSerifText(
            "苹果电脑",
            t2c={"苹果电脑": YELLOW,
                 "AIPC": RED,
                 "先进": BLUE}
        ).scale(2)
        svg_image = SVGMobject(
            "D:\\Downloads\\4=1+1+4-5-1+4.svg",
            color=BLUE,
            stroke_width=0

        ).scale(0.4)

        self.play(Write(text1))
        self.wait(3)
        self.play(FadeOutAndShiftDown(text1))
        self.wait(3)
        self.play(Write(AIPC))
        self.wait(1)
        self.play(Transform(AIPC, four))
        self.wait(1)
        self.play(FadeOutAndShiftDown(AIPC))
        self.play(Write(
            svg_image,
            run_time=5
        ))
        self.wait(3)
        self.play(Transform(svg_image, four))
        self.wait(1)
        self.play(Transform(svg_image, applePC))
        self.wait(3)
        self.play(FadeOutAndShiftDown(svg_image))


class TempClass2(Scene):
    def construct(self):
        textTest = TextMobject(
            "test",
            background_stroke_color=RED
        )
        text1 = SouseHanSerifText(
            "MacBook单管压i9 非常的先进",
            t2c={
                "MacBook": YELLOW,
                "先进": BLUE
            }
        ).shift(UP * 2.5)

        text2 = SouseHanSerifText(
            "AIPC采用了两个3.5mm音频接口 是双倍的先进",
            t2c={
                "MacBook": YELLOW,
                "AIPC": RED,
                "先进": BLUE
            }
        ).shift(UP * 2.5)
        self.play(ShowCreation(text1))
        self.wait(3)
        self.play(Transform(text1, text2))
        self.wait(3)
        self.play(Uncreate(text1))
        self.wait(1)


class TempClass1(Scene):
    def construct(self):
        text1 = SouseHanSerifText(
            "接下来为您介绍",
            t2c={
                "介绍": BLUE
            }
        ).scale(2)
        text2 = SouseHanSerifText(
            "AIPC MacBook 说",
            t2c={"AIPC": RED,
                 "MacBook": YELLOW
                 }
        ).scale(2)
        self.play(Write(text1))
        self.wait(1)
        self.play(Transform(text1, text2))
        self.wait(2)


class PrintTexts(Scene):
    def construct(self):
        souseHanText = SouseHanSerifText("本视频不求三连 觉得有道理随缘给就行\n\n本视频一部分动画采用了Manim（比我想象中的麻烦的多）\n\n感谢你看我发牢骚")

        self.play(Write(souseHanText))
