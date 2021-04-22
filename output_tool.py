import ctypes  # 用于适配DPI
import os
import pathlib
import time
import tkinter.messagebox
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.ttk import *  # 用于tkinter的美化

from windnd import windnd

'''lang_dict_sc = {
    'title': '繁简转换GUI', 'Beth': '9102', 'Cecil': '3258'
}'''

root_frame = Tk()
# root_frame.iconbitmap('.\\ji.ico')

# DPI适配
# 告诉操作系统使用程序自身的dpi适配
ctypes.windll.shcore.SetProcessDpiAwareness(1)
# 获取屏幕的缩放因子
ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
# 设置程序缩放
root_frame.tk.call('tk', 'scaling', ScaleFactor / 75)

root_frame.title('Manim output tool')
file_frame = Frame(root_frame)



root_frame.mainloop()
