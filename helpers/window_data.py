from tkinter import *

isForPreviewing = IntVar()
isTransparent = IntVar()
outputQuality = StringVar()
sceneClassName = StringVar()


def getArguments():
    arguments = ""
    if isTransparent.get() == 1:
        arguments += " --transparent"
    if isForPreviewing.get() == 1:
        arguments += " --preview"
        arguments += " --resolution 2160,3840"
    return arguments
