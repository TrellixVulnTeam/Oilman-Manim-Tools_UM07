# -*- coding: gbk -*-
#############
from manimlib.imports import *
from workspace.a_lot_of_assets.fonts_for_manim import SouseHanSerifText
class PrintTexts(Scene):
    def construct(self):
        text = SouseHanSerifText("支持中文").scale(4.0)
        self.play(Write(text))
        self.wait(3.0)
#############