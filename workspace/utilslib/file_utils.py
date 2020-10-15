import os
import shutil
from datetime import datetime


def get_name(dir, qualityName, fileName):
    now_time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    s = "%s_%s_%s%s" % (os.path.splitext(fileName)[0], qualityName, now_time, os.path.splitext(fileName)[1])
    return os.path.join(dir, s)  # 返回新文件路径


def get_new_name_with_copy(dir, f):
    if os.path.exists(os.path.join(dir, f)):
        s = "%s_%s%s" % (os.path.splitext(f)[0], 'Copy', os.path.splitext(f)[1])
        return get_new_name_with_copy(dir, s)  # 新命名文件是否存在
    return os.path.join(dir, f)  # 返回新文件路径


def video_output_helper(sceneClassName, pyFileName, arguments, argumentsForCopy):
    print('Final argument is: ' + arguments)

    manimPath = '"C:\Program Files\Python37\Lib\manim\manim.py"'

    CMDInput = '%s %s %s %s%s' % ('python', manimPath, pyFileName, sceneClassName, arguments)

    os.system(CMDInput)
    video_copy_helper(sceneClassName, arguments, argumentsForCopy)


def video_copy_helper(sceneClassName, arguments, argumentsForCopy):
    if arguments.__contains__("--low_quality"):
        defaultPath = '%s%s%s' % (os.getcwd(), '\\output\\', 'low\\')

    else:
        defaultPath = '%s%s' % (os.getcwd(), '\\output\\')

    inputFileDirRoot = inputFileDir = '%s%s%s' % (os.getcwd(), '\\media\\videos\\', 'animation\\')

    inputFileName = ''
    if arguments.__contains__(" --transparent"):
        inputFileName = '%s%s' % (sceneClassName, '.mov')
    else:
        inputFileName = '%s%s' % (sceneClassName, '.mp4')

    qualityName = ''
    if arguments.__contains__(' --low_quality'):
        qualityName = '480p15'
    if arguments.__contains__(' --high_quality'):
        qualityName = '1080p60'
    if arguments.__contains__(' --resolution 2160,3840'):
        qualityName = '2160p60'

    outFileDir = get_name(dir=defaultPath,
                          qualityName=qualityName,
                          fileName=inputFileName)
    inputFileDir = r'%s%s%s' % (inputFileDirRoot, qualityName + '\\', inputFileName)

    shutil.copy(inputFileDir, outFileDir)
    if argumentsForCopy.__contains__('-show_in_explorer'):
        os.startfile(defaultPath)




