import os
import shutil
import tkinter

from tkinter import *
import tkinter.messagebox

import utilslib.file_utils


def printState():
    print('Argument is: ' + getArguments())


def videoOut():
    global argsForQuality

    print('Final argument is: ' + getArguments())

    manimPath = '"C:\Program Files\Python37\Lib\manim\manim.py"'
    pyFileName = 'animation.py'
    sceneClassName = 'PrintTexts'
    CMDInput = '%s %s %s %s%s' % ('python', manimPath, pyFileName, sceneClassName, getArguments())

    os.system(CMDInput)
    if outputQuality.get() == 0:
        defaultPath = '%s%s%s' % (os.getcwd(), '\\output\\', 'low\\')

    else:
        defaultPath = '%s%s' % (os.getcwd(), '\\output\\')

    inputFileDirRoot = inputFileDir = '%s%s%s' % (os.getcwd(), '\\media\\videos\\', 'animation\\')

    inputFileName = ''
    if getArguments().__contains__(" --transparent"):
        inputFileName = '%s%s' % (sceneClassName, '.mov')
    else:
        inputFileName = '%s%s' % (sceneClassName, '.mp4')

    qualityName = ''
    if getArguments().__contains__(' --low_quality'):
        qualityName = '480p15'
    if getArguments().__contains__(' --high_quality'):
        qualityName = '1080p60'
    if getArguments().__contains__(' --resolution 2160,3840'):
        qualityName = '2160p60'

    outFileDir = utilslib.file_utils.get_name(dir=defaultPath,
                                              qualityName=qualityName,
                                              fileName=inputFileName)
    inputFileDir = r'%s%s%s' % (inputFileDirRoot, qualityName + '\\', inputFileName)

    shutil.copy(inputFileDir, outFileDir)


def getArguments():
    arguments = ""
    if isTransparent.get() == 1:
        arguments += " --transparent"
    if isForPreviewing.get() == 1:
        arguments += " --preview"
    if outputQuality.get() == qualityDic.get('low'):
        arguments += " --low_quality"
    if outputQuality.get() == qualityDic.get('high'):
        arguments += " --high_quality"
    if outputQuality.get() == qualityDic.get('4k'):
        arguments += " --resolution 2160,3840"
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

################################################
# left frame
leftFrame = Frame(root)
leftFrame.place(relx=0.0)
# bottom
bottom = Button(leftFrame,
                text="Output",
                command=videoOut
                )
bottom.pack(fill=Y)

################################################
# right frame
rightFrame = Frame(root)
rightFrame.place(relx=0.5)
# quality selection
qualityDic = {'low': 0, 'high': 1, '4k': 2}
outputQuality = IntVar()
lowQualityRadioBottom = Radiobutton(rightFrame, text="Low Quality",
                                    variable=outputQuality,
                                    value=qualityDic.get('low'),
                                    command=printState
                                    )
lowQualityRadioBottom.pack()

HighQualityRadioBottom = Radiobutton(rightFrame, text="High Quality",
                                     variable=outputQuality,
                                     value=qualityDic.get('high'),
                                     command=printState
                                     )
HighQualityRadioBottom.pack()

UHDQualityRadioBottom = Radiobutton(rightFrame, text="4K",
                                    variable=outputQuality,
                                    value=qualityDic.get('4k'),
                                    command=printState
                                    )
UHDQualityRadioBottom.pack()

# Other options
isForPreviewing = IntVar()
previewCheckBox = Checkbutton(rightFrame, text='preview',
                              variable=isForPreviewing,
                              onvalue=1, offvalue=0,
                              command=printState)
previewCheckBox.select()
previewCheckBox.pack(fill=X)

isTransparent = IntVar()
transparentCheckBox = Checkbutton(rightFrame, text='transparent',
                                  variable=isTransparent,
                                  onvalue=1, offvalue=0,
                                  command=printState)
transparentCheckBox.pack()

root.mainloop()
