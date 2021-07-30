import ctypes  # 用于适配DPI
import os
import pathlib
import threading
import time
import tkinter.messagebox
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.ttk import *  # 用于tkinter的美化
from windnd import windnd

import ast

"""
Version 0.1.0
This is the py file for the GUI output tool
Works with Manim 1.0.0
"""


class ValueHolder:
    quality_options = ['--uhd', "-l", '-m', '--hd']
    """
    -w to write the scene to a file
    -o to write the scene to a file and open the result
    -s to skip to the end and just show the final frame.
    -so will save the final frame to an image and show it
    -n <number> to skip ahead to the n'th animation of a scene.
    -f to make the playback window fullscreen
    """
    write_options = ['-o', '-w', '']
    animation_class_names = []
    out_quality_argument = ""
    write_argument = ""


print(time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(time.time())))


def get_classes_names(source: str):
    p = ast.parse(source)
    classes = [node.name for node in ast.walk(p) if isinstance(node, ast.ClassDef)]
    # print("=====")
    # print(classes)
    # print("=====")
    return classes
    # ['test', 'test2', 'inner_class']


def open_animation_file_in_str(animation_file_name: str):
    with open(animation_file_name, 'r', encoding='utf-8') as file:
        animation_str = file.read()
    return animation_str


def get_all_py_files():
    output = []
    for current_file in os.listdir():
        if current_file.endswith('.py'):
            output.append(current_file)
    return output


def py_file_combobox_select_event(*args):
    selected_file_name = py_file_combobox.get()
    # print(selected_file_name)
    selected_file_content = open_animation_file_in_str(selected_file_name)
    # print(selected_file_content)
    # print(get_classes_names(selected_file_content))
    try:
        animation_class_combobox["values"] = get_classes_names(selected_file_content)
    except NameError:
        ValueHolder.animation_class_names = get_classes_names(selected_file_content)


def quality_combobox_select_event(*args):
    ValueHolder.out_quality_argument = quality_combobox.get()
    print(ValueHolder.out_quality_argument)


def get_cmd_arguments():
    cmd_arguments = '%s %s %s %s %s' % ('manimgl', py_file_combobox.get(), animation_class_combobox.get(),
                                        ValueHolder.write_argument,
                                        ValueHolder.out_quality_argument
                                        )
    print(time_stamp_check_var)
    if time_stamp_check_var.get() == 1:
        cmd_arguments = ''.join(
            [cmd_arguments,
             " --file_name ",
             animation_class_combobox.get(),
             "_",
             time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(time.time())),
             ])
    if transparent_check_var.get() == 1:
        cmd_arguments = ''.join([cmd_arguments, ' --transparent'])
    return cmd_arguments


def animation_class_combobox_select_event(*args):
    pass


def write_combobox_select_event(*args):
    ValueHolder.write_argument = write_combobox.get()


def output_task(*args):
    os.system(get_cmd_arguments())


def output_button_event():
    if animation_class_combobox.get() == '':
        messagebox.showwarning("Warning", "Please select an animation class!")
        return

    print("".join(['The final argument is: ', get_cmd_arguments()]))

    output = threading.Thread(target=output_task, args=(1,))
    output.start()


py_files = get_all_py_files()

root_frame = Tk()

# DPI适配
# 告诉操作系统使用程序自身的dpi适配
ctypes.windll.shcore.SetProcessDpiAwareness(1)
# 获取屏幕的缩放因子
ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
# 设置程序缩放
root_frame.tk.call('tk', 'scaling', ScaleFactor / 75)

root_frame.title('Manim output tool')
file_frame = Frame(root_frame)

# Animation file combobox
py_file_label = Label(root_frame, text='Animation File')
py_file_label.pack()
py_file_combobox = Combobox(root_frame, values=py_files)
py_file_combobox.current(0)
py_file_combobox.bind("<<ComboboxSelected>>", py_file_combobox_select_event)
py_file_combobox_select_event()
py_file_combobox.pack()

# Animation class combobox
animation_class_label = Label(root_frame, text='Animation Class')
animation_class_label.pack()
animation_class_combobox = Combobox(root_frame, values=ValueHolder.animation_class_names)
# animation_class_combobox.current(0)
animation_class_combobox.bind("<<ComboboxSelected>>", py_file_combobox_select_event)
animation_class_combobox_select_event()
animation_class_combobox.pack()

# Output options
# Quality #
quality_label = Label(root_frame, text='Quality Option')
quality_label.pack()
quality_combobox = Combobox(root_frame, values=ValueHolder.quality_options)
quality_combobox.current(0)
quality_combobox.bind("<<ComboboxSelected>>", quality_combobox_select_event)
quality_combobox_select_event()
quality_combobox.pack()
#
write_label = Label(root_frame, text='Write Option')
write_label.pack()
write_combobox = Combobox(root_frame, values=ValueHolder.write_options)
write_combobox.current(0)
write_combobox.bind("<<ComboboxSelected>>", write_combobox_select_event)
write_combobox_select_event()
write_combobox.pack()

# Time Stamp
time_stamp_check_var = IntVar()
time_stamp_check_box = Checkbutton(root_frame,
                                   text='add time stamp in name',
                                   variable=time_stamp_check_var,
                                   onvalue=1, offvalue=0
                                   )
time_stamp_check_var.set(1)
time_stamp_check_box.pack()

# Transparent
transparent_check_var = IntVar()
transparent_check_box = Checkbutton(root_frame,
                                    text='Transparent',
                                    variable=transparent_check_var,
                                    onvalue=1, offvalue=0
                                    )
transparent_check_var.set(0)
transparent_check_box.pack()

# Output button
output_button = Button(root_frame, text='Output', command=output_button_event)
output_button.pack()
#
# output_progress = Progressbar(root_frame, orient=HORIZONTAL,
#                               length=400, mode='determinate')
# output_progress.pack()

root_frame.mainloop()
