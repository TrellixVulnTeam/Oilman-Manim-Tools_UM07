from manimlib import *


# https://fonts.google.com/specimen/Noto+Serif+SC
class SourceHanSerifTextScHeavy(Text):
    CONFIG = {
        'font': 'Source Han Serif SC',
        "weight": "HEAVY"
    }


class SourceHanSerifTextScBold(Text):
    CONFIG = {
        'font': 'Source Han Serif SC',
        "weight": BOLD
    }


class SourceHanSerifTextScNormal(Text):
    CONFIG = {
        'font': 'Source Han Serif CN',
        "weight": NORMAL
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
        'font': 'Source Han Sans SC'
    }


class TimesNewRomanText(Text):
    CONFIG = {
        'font': 'Times New Roman'
    }
