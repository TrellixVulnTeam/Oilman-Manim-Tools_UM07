from manim.manimlib.animation.creation import Write
from manim.manimlib.scene.scene import Scene
from workspace.utils import fonts_for_manim


class PrintTexts(Scene):

    def construct(self):
        text = fonts_for_manim.SouseHanSerif("%s")
        self.play(Write(text))
