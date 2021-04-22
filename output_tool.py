import ctypes  # 用于适配DPI
import os
import pathlib
import time
import tkinter.messagebox
from tkinter import *
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
    animation_class_names = []


def get_classes_names(source: str):
    p = ast.parse(source)
    classes = [node.name for node in ast.walk(p) if isinstance(node, ast.ClassDef)]
    print("=====")
    print(classes)
    print("=====")
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
    ValueHolder.animation_class_names = get_classes_names(selected_file_content)


def animation_class_combobox_select_event(*args):
    pass


print(get_all_py_files())

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

animation_class_label = Label(root_frame, text='Animation Class')
animation_class_label.pack()
animation_class_combobox = Combobox(root_frame, values=ValueHolder.animation_class_names)
animation_class_combobox.current(0)
animation_class_combobox.bind("<<ComboboxSelected>>", py_file_combobox_select_event)
animation_class_combobox_select_event()
animation_class_combobox.pack()

root_frame.mainloop()
