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

class_names = []


def get_classes_name(source: str):
    p = ast.parse(source)
    classes = [node.name for node in ast.walk(p) if isinstance(node, ast.ClassDef)]
    # ['test', 'test2', 'inner_class']


def open_animation_file_in_str(animation_file_name: str):
    with open(animation_file_name, 'r') as file:
        animation_str = file.read().replace('\n', '')


def get_all_py_files():
    output = []
    for current_file in os.listdir():
        if current_file.endswith('.py'):
            output.append(current_file)
    return output


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

py_file_button = Combobox(root_frame)
py_file_button['values'] = py_files
py_file_button.current(0)

py_file_button.pack()

root_frame.mainloop()
