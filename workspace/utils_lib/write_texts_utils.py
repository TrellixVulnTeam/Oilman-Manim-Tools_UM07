import os

from workspace.utils_lib.file_utils import video_output_helper


def make_temp_animation_file(text, scaleNum, waitTime):
    template_file_name = '%s%s' % (os.getcwd(), '\\a_lot_of_assets\\write.py.template')
    templateFile = open(template_file_name, mode='r')
    templateFileStr = templateFile.read()
    #  replacing keywords
    tempStr = templateFileStr.replace('%Texts', text).replace('%ScaleNum', str(scaleNum)).replace('%WaitTime',
                                                                                                  str(waitTime))

    print('temp file content is: \n' + tempStr)
    templateFile.close()
    temp_file_name = '%s%s' % (os.getcwd(), '\\TEMP\\temp_write.py')
    tempAnimationFile = open(temp_file_name, mode='w')
    tempAnimationFile.write(tempStr)
    templateFile.close()


def make_animation(sceneClassName='PrintTexts', arguments=' --low_quality -p', argumentsForCopy='-show_in_explorer'):
    video_output_helper(sceneClassName, pyFileName='%s%s' % (os.getcwd(), '\\TEMP\\temp_write.py'), arguments=arguments,
                        argumentsForCopy=argumentsForCopy)


def make_writing_animation(text='Your Texts Here', scaleNum=2.0, waitTime=1.0, argumentsForManim=' --low_quality -p', argumentsForCopy='-show_in_explorer'):
    make_temp_animation_file(text, scaleNum, waitTime)
    make_animation(arguments=argumentsForManim, argumentsForCopy=argumentsForCopy)
