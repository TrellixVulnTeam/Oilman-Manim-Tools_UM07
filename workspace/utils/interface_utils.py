import os
from datetime import datetime


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
