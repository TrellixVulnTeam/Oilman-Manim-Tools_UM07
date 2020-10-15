import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import tkinter

from tkinter import *
import tkinter.messagebox

from workspace.utils_lib.write_texts_utils import make_writing_animation


def printState():
    print('Argument is: ' + getArguments())


def videoOut():
    make_writing_animation(text=userInputText.get(),
                           scaleNum=float(textSizeInputStr.get()),
                           waitTime=float(waitTimeStr.get()),
                           argumentsForManim=getArguments(),
                           argumentsForCopy=showInExplorer.get()
                           )


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
leftFrame.place(relx=0.1)

# user input #############
# label
userInputTextLabel = Label(leftFrame, text='Texts you want to write')
userInputTextLabel.pack()
# entry
userInputText = StringVar()
userInputText.set('Your Texts Here')
sceneClassNameInput = Entry(leftFrame,
                            exportselection=0,  # 默认情况下，你如果在输入框中选中文本，默认会复制到粘贴板，如果要忽略这个功能刻工艺设置 exportselection=0。
                            textvariable=userInputText
                            )

sceneClassNameInput.pack(fill=X)
# label
textSizeInputLabel = Label(leftFrame, text='Texts Size')
textSizeInputLabel.pack()
# entry
textSizeInputStr = StringVar()
textSizeInputStr.set('2')
textSizeInput = Entry(leftFrame,
                      exportselection=0,  # 默认情况下，你如果在输入框中选中文本，默认会复制到粘贴板，如果要忽略这个功能刻工艺设置 exportselection=0。
                      textvariable=textSizeInputStr
                      )
textSizeInput.pack(fill=X)
# label
waitTimeLabel = Label(leftFrame, text='Wait Time')
waitTimeLabel.pack()
# entry
waitTimeStr = StringVar()
waitTimeStr.set('1')
waitTimeInput = Entry(leftFrame,
                      exportselection=0,  # 默认情况下，你如果在输入框中选中文本，默认会复制到粘贴板，如果要忽略这个功能刻工艺设置 exportselection=0。
                      textvariable=waitTimeStr
                      )
waitTimeInput.pack(fill=X)
# Output Bottom #############
outputBottomLabel = Label(leftFrame,
                          text='\n')
outputBottomLabel.pack()
# bottom
outputBottom = Button(leftFrame,
                      text="Output",
                      command=videoOut
                      )
outputBottom.pack(fill=X)

################################################
# right frame
rightFrame = Frame(root)
rightFrame.place(relx=0.5)

# quality selection
# label
qualitySelectionLabel = Label(rightFrame, text='Quality Selection')
qualitySelectionLabel.pack(fill=X)
# radio bottom
qualityDic = {'low': 0, 'high': 1, '4k': 2}
outputQuality = IntVar()
lowQualityRadioBottom = Radiobutton(rightFrame, text="Low Quality",
                                    variable=outputQuality,
                                    value=qualityDic.get('low'),
                                    command=printState
                                    )
lowQualityRadioBottom.pack(fill=X)

HighQualityRadioBottom = Radiobutton(rightFrame, text="High Quality",
                                     variable=outputQuality,
                                     value=qualityDic.get('high'),
                                     command=printState
                                     )
HighQualityRadioBottom.pack(fill=X)

UHDQualityRadioBottom = Radiobutton(rightFrame, text="4K",
                                    variable=outputQuality,
                                    value=qualityDic.get('4k'),
                                    command=printState
                                    )
UHDQualityRadioBottom.pack(fill=X)

# Other options
otherOptionsLabel = Label(rightFrame, text='Other Options')
otherOptionsLabel.pack(fill=X)
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

showInExplorer = StringVar()
showInExplorerCheckBox = Checkbutton(rightFrame, text='Show in Explorer',
                                     variable=showInExplorer,
                                     onvalue="--show_in_explorer", offvalue='',
                                     command=printState)
showInExplorerCheckBox.pack()

root.mainloop()
