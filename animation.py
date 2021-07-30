from manimlib import *

from fonts import *

'''
manimgl animation.py Theary
Preview

-w to write the scene to a file

-o to write the scene to a file and open the result

'''


class NumberAnimation(Scene):
    def construct(self):
        linux = TimesNewRomanText(
            'Linux',
            color=BLUE,
            font_size=80
        )
        five = TimesNewRomanText(
            '5',
            color=TEAL,
            font_size=80
        )
        number_theory_1 = TimesNewRomanText(
            '5 = 1 + 1 + 4 - 5 + 1 × 4',
            t2c={'[:1]': TEAL},
            font_size=80
        )
        number_theory_2 = TimesNewRomanText(
            '1 + 1 + 4 - 5 + 1 × 4',
            font_size=80
        )
        number_theory_3 = TimesNewRomanText(
            '1 + 1 + 4 - 5 - 1 × 4',
            font_size=80
        )
        number_theory_4 = TimesNewRomanText(
            '1 + 1 + 4 - 5 - 1 + 4',
            font_size=80
        )
        number_theory_5 = TimesNewRomanText(
            '1 + 1 + 4 - 5 - 1 + 4 = 4',
            font_size=80,
            t2c={'[24:]': GOLD},
        )

        four = TimesNewRomanText(
            "4",
            font_size=80,
            color=GOLD
        )
        bios = TimesNewRomanText(
            "BIOS",
            font_size=80,
            color=GOLD
        )
        self.play(Write(linux))
        self.wait(1)
        self.play(Transform(linux, five))
        self.wait()
        self.play(Transform(linux, number_theory_1))
        self.wait()
        self.play(Transform(linux, number_theory_2))
        self.wait()
        self.play(Transform(linux, number_theory_3))
        self.wait()
        self.play(Transform(linux, number_theory_4))
        self.wait()
        self.play(Transform(linux, number_theory_5))
        self.wait()
        self.play(Transform(linux, four))
        self.wait()
        self.play(Transform(linux, bios))
        self.wait()


class Theory(Scene):
    def construct(self):
        a = 'Linux'
        b = 'BIOS'
        x = '精简'
        a_is_x = SourceHanSerifTextScNormal(
            "Linux 很精简",
            t2c={a: BLUE, x: TEAL},
            font_size=96,
        )
        b_is_also_x = SourceHanSerifTextScNormal(
            "BIOS 也很精简",
            t2c={b: GOLD, x: TEAL},
            font_size=96
        )
        self.play(Write(a_is_x))
        self.wait(1)
        self.play(Transform(a_is_x, b_is_also_x))
        self.wait(1)
        self.play(Uncreate(a_is_x))


class WriteSomething(Scene):
    def construct(self):
        text_to_write = TimesNewRomanText(
            'Los Alamos National Laboratory',
            font_size=70,
            color=BLUE
        )
        self.play(Write(text_to_write))
        self.wait(1)
        self.play(Uncreate(text_to_write))


'''
Some fonts
'''
