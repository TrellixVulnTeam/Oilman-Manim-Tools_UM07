import os
import shutil
from manim.manimlib.animation.creation import Write

import copy_helper
import fonts

from tkinter import *
from manimlib.scene.scene import Scene


def printState():
    print('Argument is: ' + getArguments())


def videoOut():
    global argsForQuality

    print('Final argument is: ' + getArguments())

    os.system(
        'python "C:\Program Files\Python37\Lib\manim\manim.py" test.py PrintTexts' + getArguments())
    if outputQuality.get() == 0:
        defaultPath = '%s%s%s' % (os.getcwd(), '\\output\\', 'low\\')

    else:
        defaultPath = '%s%s' % (os.getcwd(), '\\output\\')
    outFileDir = copy_helper.get_new_name(dir=defaultPath, f='manim.mp4')
    inputFileDir = r'%s%s%s%s%s' % (os.getcwd(), '\\media\\videos\\', 'test\\', '480p15\\', 'PrintTexts.mp4')
    shutil.copy(inputFileDir, outFileDir)


def getArguments():
    global argsForOutput

    arguments = ""
    if isTransparent.get() == 1:
        arguments += " -t"
    if isForPreviewing.get() == 1:
        arguments += " -p"
    if outputQuality.get() == 0:
        arguments += " -l"
    if outputQuality.get() == 1:
        arguments += " --high_quality"
    return arguments




# menu
def popupmenu(event):
    mainMenu.post(event.x_root, event.y_root)


# GUI
root = Tk()
root.geometry('320x240')
root.title('Manim Helper')

mainMenu = Menu(root)
debugMenu = Menu(mainMenu)
mainMenu.add_cascade(label="debug", menu=debugMenu)
debugMenu.add_command(label="printState", command=printState)
debugMenu.add_separator()  # 分割线
debugMenu.add_command(label="exit", command=root.destroy)
root.config(menu=mainMenu)
root.bind('Button-3', popupmenu)

bottom = Button(root,
                text="Output",
                command=lambda: videoOut()
                )
bottom.place(relx=0.25, rely=0.6, relwidth=0.5, relheight=0.3)

outputQuality = IntVar()
lowQualityRadioBottom = Radiobutton(root, text="Low Quality",
                                    variable=outputQuality,
                                    value=0,
                                    )
lowQualityRadioBottom.pack()

HighQualityRadioBottom = Radiobutton(root, text="High Quality",
                                     variable=outputQuality,
                                     value=1,
                                     )
HighQualityRadioBottom.pack()

isForPreviewing = IntVar()
previewCheckBox = Checkbutton(root, text='preview', variable=isForPreviewing, onvalue=1, offvalue=0)
previewCheckBox.select()
previewCheckBox.pack()

isTransparent = IntVar()
transparentCheckBox = Checkbutton(root, text='transparent', variable=isTransparent, onvalue=1, offvalue=0)
transparentCheckBox.pack()

root.mainloop()


class PrintTexts(Scene):

    def construct(self):
        text = fonts.SouseHanSerif("本视频不求三连 觉得有道理随缘给就行\n\n本视频一部分动画采用了Manim（比我想象中的麻烦的多）\n\n感谢你看我发牢骚")
        self.play(Write(text))
