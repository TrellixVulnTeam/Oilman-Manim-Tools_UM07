from tkinter import *

from window_data import outputQuality


def printState():
    print('Argument is: ' + outputQuality.get())


def addBottoms(frame, outputQualityIn):
    outputQuality=outputQualityIn
    # label
    qualitySelectionLabel = Label(frame, text='Quality Selection')
    qualitySelectionLabel.pack(fill=X)
    # radio bottom
    # qualityDic = {'low': 0, 'high': 1, '4k': 2}
    # outputQuality = IntVar()
    lowQualityRadioBottom = Radiobutton(frame, text="Low Quality",
                                        variable=outputQuality,
                                        value=" --low_quality",
                                        command=printState
                                        )
    lowQualityRadioBottom.pack(fill=X)

    HighQualityRadioBottom = Radiobutton(frame, text="High Quality",
                                         variable=outputQuality,
                                         value=" --high_quality",
                                         command=printState
                                         )
    HighQualityRadioBottom.pack(fill=X)

    UHDQualityRadioBottom = Radiobutton(frame, text="4K",
                                        variable=outputQuality,
                                        value=" --resolution 2160,3840",
                                        command=printState
                                        )
    UHDQualityRadioBottom.pack(fill=X)
    # return frame


def getArgument():
    return outputQuality
