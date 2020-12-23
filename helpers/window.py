import os
import shutil
import tkinter

from tkinter import *
import tkinter.messagebox

import output_file_helper
import quality_selection_radio_bottoms
from window_data import outputQuality, sceneClassName, isTransparent, isForPreviewing


def videoOut():
    output_file_helper.video_output_helper(sceneClassName=sceneClassName.get(),
                                           pyFileName='animations.py',  # name of animation file
                                           arguments=getArguments(),
                                           argumentsForCopy=showInExplorer.get()
                                           )


def printState():
    print('Argument is: ' + getArguments())


def getArguments():
    arguments = ""
    if isTransparent.get() == 1:
        arguments += " --transparent"
    if isForPreviewing.get() == 1:
        arguments += " --preview"
    # if outputQuality.get() == qualityDic.get('low'):
    #     arguments += " --low_quality"
    # if outputQuality.get() == qualityDic.get('high'):
    #     arguments += " --high_quality"
    # if outputQuality.get() == qualityDic.get('4k'):
        arguments += outputQuality.get()
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

# Scene Class Name #############
# label
sceneClassNameInputLabel = Label(leftFrame, text='Scene Class Name')
sceneClassNameInputLabel.pack()
# entry
# sceneClassName = StringVar()
sceneClassName.set('PrintTexts')
sceneClassNameInput = Entry(leftFrame,
                            exportselection=0,  # 默认情况下，你如果在输入框中选中文本，默认会复制到粘贴板，如果要忽略这个功能刻工艺设置 exportselection=0。
                            textvariable=sceneClassName
                            )

sceneClassNameInput.pack(fill=X)
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
# outputQuality = StringVar()

quality_selection_radio_bottoms.addBottoms(rightFrame)

# lowQualityRadioBottom = Radiobutton(rightFrame, text="Low Quality",
#                                     variable=outputQuality,
#                                     value=qualityDic.get('low'),
#                                     command=printState("-low")
#                                     )
# lowQualityRadioBottom.pack(fill=X)
#
# HighQualityRadioBottom = Radiobutton(rightFrame, text="High Quality",
#                                      variable=outputQuality,
#                                      value=qualityDic.get('high'),
#                                      command=printState('-high')
#                                      )
# HighQualityRadioBottom.pack(fill=X)
#
# UHDQualityRadioBottom = Radiobutton(rightFrame, text="4K",
#                                     variable=outputQuality,
#                                     value=qualityDic.get('4k'),
#                                     command=printState('4k')
#                                     )
# UHDQualityRadioBottom.pack(fill=X)

# Other options
otherOptionsLabel = Label(rightFrame, text='Other Options')
otherOptionsLabel.pack(fill=X)
# isForPreviewing = IntVar()
previewCheckBox = Checkbutton(rightFrame, text='preview',
                              variable=isForPreviewing,
                              onvalue=1, offvalue=0,
                              command=printState)
previewCheckBox.select()
previewCheckBox.pack(fill=X)

# isTransparent = IntVar()
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
