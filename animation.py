from manimlib import *

'''
manimgl animation.py Out
Preview

-w to write the scene to a file

-o to write the scene to a file and open the result

'''


class Out(Scene):
    def construct(self):
        text = SourceHanSerifText(
            "论证完毕",
            color=BLUE
        ).scale(3)
        text2 = SourceHanSerifText(
            "QED",
            color=RED
        ).scale(3)
        self.play(Write(text))
        self.wait(1)
        self.play(Transform(text, text2))
        self.wait(1)


'''
Some fonts
'''


# https://fonts.google.com/specimen/Noto+Serif+SC
class SourceHanSerifText(Text):
    CONFIG = {
        'font': 'Source Han Serif SC',
        'weight': BOLD
    }


# https://fonts.google.com/specimen/ZCOOL+KuaiLe
# https://www.zcool.com.cn/special/zcoolfonts/
class HappyZcoolText(Text):
    CONFIG = {
        'font': 'HappyZcool-2016'
    }


# https://fonts.google.com/specimen/Noto+Sans+SC
class SouseHanSansText(Text):
    CONFIG = {
        'font': 'Noto Sans SC Black'
    }


class TimesNewRomanText(Text):
    CONFIG = {
        'font': 'Times New Roman'
    }
