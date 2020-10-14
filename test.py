from manimlib.imports import*

class HelloWorld(Scene):
    def construct(self):
        souseHanText1 =SouseHanText("何同学").scale(4)

        souseHanText2 =SouseHanText("540万粉丝",color=BLUE).scale(4)

        souseHanText3 =SouseHanText("1800脑残",color=RED).scale(4)

        rectangle = Rectangle(color=BLUE)

        rectangle.surround(souseHanText2)

        
        self.play(Write(souseHanText1))
        self.wait(1)
        self.play(FadeIn(rectangle))
        self.wait(3)
        self.play(Transform(souseHanText1, souseHanText2))
        self.wait(1)
        self.play(Transform(souseHanText1, souseHanText3))
        self.wait(1)



class TransformTexts(Scene):
    def construct(self):
        text = SouseHanText("我们都是在否定中不断成长的").scale(2)
        text2 = SouseHanText("自己的", color=BLUE).scale(3)
        text3 = SouseHanText("他人的", color=RED).scale(3)

        self.play(Write(text))
        self.wait(1)
        self.play(Transform(text,text2))
        self.wait(1)
        self.play(Transform(text,text3))
        self.wait(1)
        

class PrintTexts(Scene):
    def construct(self):
        souseHanText = SouseHanText("本视频不求三连 觉得有道理随缘给就行\n\n本视频一部分动画采用了Manim（比我想象中的麻烦的多）\n\n感谢你看我发牢骚")

        self.play(Write(souseHanText))


class SouseHanText(Text):
    CONFIG = {
        'font' : 'Noto Serif SC Black'
    }
        #'font' : 'HappyZcool-2016'
