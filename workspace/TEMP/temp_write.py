# -*- coding: gbk -*-
#############
from manimlib.imports import *
from workspace.assets.fonts_for_manim import SouseHanSerifText
class PrintTexts(Scene):
    def construct(self):
        text = SouseHanSerifText("Your Texts Here").scale(2.0)
        self.play(Write(text))
        self.wait(1.0)
#############