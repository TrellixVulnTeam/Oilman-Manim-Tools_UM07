import os
import shutil
import tkinter

from tkinter import *
import tkinter.messagebox

from workspace.utils.file_utils import get_name


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

    if getArguments().__contains__("-t"):
        outFileDir = get_name(dir=defaultPath, f='manim.mov')
        inputFileDir = r'%s%s%s%s%s' % (os.getcwd(), '\\media\\videos\\', 'test\\', '480p15\\', 'PrintTexts.mov')
    else:
        outFileDir = get_name(dir=defaultPath, f='manim.mp4')
        inputFileDir = r'%s%s%s%s%s' % (os.getcwd(), '\\media\\videos\\', 'test\\', '480p15\\', 'PrintTexts.mp4')

    shutil.copy(inputFileDir, outFileDir)


def getArguments():
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
def topMenu(event):
    mainMenu.post(event.x_root, event.y_root)


def popMessagebox():
    answer = tkinter.messagebox.askokcancel('About',
                                            'Manim output helper\n' +
                                            'made by Oilman')


# GUI
root = Tk()
root.geometry('320x240')
root.title('Manim Helper')

# menu
mainMenu = Menu(root)
debugMenu = Menu(mainMenu)
mainMenu.add_cascade(label="Debug", menu=debugMenu)
debugMenu.add_command(label="printState", command=printState)
debugMenu.add_separator()  # 分割线
debugMenu.add_command(label="exit", command=root.destroy)

aboutMenu = Menu(mainMenu)
mainMenu.add_cascade(label="About", menu=aboutMenu)
aboutMenu.add_command(label="About", command=popMessagebox)

root.config(menu=mainMenu)
root.bind('Button-3', topMenu)

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
